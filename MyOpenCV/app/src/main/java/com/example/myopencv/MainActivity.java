package com.example.myopencv;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.Surface;
import android.view.SurfaceView;
import android.widget.Toast;

import org.opencv.android.BaseLoaderCallback;
import org.opencv.android.CameraBridgeViewBase;
import org.opencv.android.OpenCVLoader;
import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.MatOfRect;
import org.opencv.core.Point;
import org.opencv.core.Rect;
import org.opencv.core.Scalar;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;
import org.opencv.objdetect.CascadeClassifier;

import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity implements CameraBridgeViewBase.CvCameraViewListener2 {
    CameraBridgeViewBase cameraBridgeViewBase;
    BaseLoaderCallback baseLoaderCallback;
    private Mat mRGB,mRGBt,mGray,mat1;
    private  int menu_option = 0;
    private CascadeClassifier faceCascade;

    public MainActivity() {
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if(OpenCVLoader.initDebug()){
            Toast.makeText(getApplicationContext(),"OK OpenCV",Toast.LENGTH_LONG).show();
        }
        else{
            Toast.makeText(getApplicationContext(),"ERROR OpenCV",Toast.LENGTH_LONG).show();
        }

        cameraBridgeViewBase= (CameraBridgeViewBase) findViewById(R.id.mycameraview);
        cameraBridgeViewBase.setVisibility(SurfaceView.VISIBLE);
        cameraBridgeViewBase.setCvCameraViewListener(this);
        baseLoaderCallback = new BaseLoaderCallback(this) {
            @Override
            public void onManagerConnected(int status) {
                //super.onManagerConnected(status);
                switch (status){
                    case BaseLoaderCallback.SUCCESS:
                        cameraBridgeViewBase.enableView();
                        break;
                    default:
                        super.onManagerConnected(status);
                        break;
                }
            }
        };
        faceCascade = new CascadeClassifier();
        faceCascade.load(getCascadeFile(R.raw.haarcascade_frontalface_alt2).getAbsolutePath());
    }

    @Override
    public void onCameraViewStarted(int width, int height) {
        mRGB = new Mat(width,height, CvType.CV_8UC4);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if(cameraBridgeViewBase!=null){
            cameraBridgeViewBase.disableView();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if(cameraBridgeViewBase!=null){
            cameraBridgeViewBase.disableView();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        if(!OpenCVLoader.initDebug()){
            Toast.makeText(getApplicationContext(),"Problema OpenCV",Toast.LENGTH_LONG).show();
        }
        else{
            baseLoaderCallback.onManagerConnected(BaseLoaderCallback.SUCCESS);
        }

        super.onResume();
    }

    @Override
    public void onCameraViewStopped() {
        mRGB.release();


    }



    @Override
    public Mat onCameraFrame(CameraBridgeViewBase.CvCameraViewFrame inputFrame) {
        mat1 = inputFrame.rgba();
        switch (menu_option){
            case 0:
                mat1 = inputFrame.rgba();break;
            case 1:
                mat1 = inputFrame.gray();break;
            case 2:
                mat1 = inputFrame.gray();
                Core.bitwise_not(mat1,mat1);
                break;
            case 3:
                //mat1 = inputFrame.rgba();
                Core.bitwise_not(mat1,mat1);
                break;
            case 4:
                //mat1 = inputFrame.rgba();
                Core.extractChannel(mat1,mat1,0);
                break;
            case 5:
                //mat1 = inputFrame.rgba();
                Core.extractChannel(mat1,mat1,1);
                break;
            case 6:
                //mat1 = inputFrame.rgba();
                Core.extractChannel(mat1,mat1,2);
                break;
            case 7:
                //mat1 = inputFrame.rgba();
                /*Imgproc.cvtColor(mat1,mat1, Imgproc.COLOR_BGR2HSV);
                List<Mat> hsvPlanes = new ArrayList<>();
                Core.split(mat1, hsvPlanes);

                Mat min_sat = new Mat();
                Imgproc.threshold(hsvPlanes.get(1), min_sat, 40,255, Imgproc.THRESH_BINARY);

                Mat max_hue = new Mat();
                Imgproc.threshold(hsvPlanes.get(0), max_hue, 15, 255, Imgproc.THRESH_BINARY_INV);

                //Mat skinHighlight = new Mat();
                Core.bitwise_and(min_sat,max_hue,mat1);*/


                Imgproc.cvtColor(mat1,mat1,Imgproc.COLOR_RGB2BGR);
                Imgproc.cvtColor(mat1,mat1,Imgproc.COLOR_BGR2HSV);
                Scalar lowerBound = new Scalar(0, 20, 70);
                Scalar upperBound = new Scalar(30, 150, 225);
                Core.inRange(mat1,lowerBound,upperBound,mat1);
                break;
            case 8:
                Imgproc.cvtColor(mat1, mat1, Imgproc.COLOR_BGR2HSV);
                Scalar lower = new Scalar(36, 0, 0);
                Scalar upper = new Scalar(86, 255, 255);
                Core.inRange(mat1, lower, upper, mat1);
                break;
            case 9:
                Imgproc.cvtColor(mat1, mat1, Imgproc.COLOR_RGBA2GRAY);
                //Mat edges = new Mat();
                Imgproc.GaussianBlur(mat1, mat1, new Size(5, 5), 1.5, 1.5);
                Imgproc.Canny(mat1, mat1, 100, 200);
                break;
            case 10:
                MatOfRect faces = new MatOfRect();
                faceCascade.detectMultiScale(mat1, faces);
                Rect[] facesArray = faces.toArray();
                for (Rect faceRect : facesArray) {
                    Imgproc.rectangle(mat1, faceRect.tl(), faceRect.br(), new Scalar(255, 0, 0), 2);
                }

                break;
        }

        Imgproc.putText(mat1,"UNI",new Point(0,mat1.height()-20),Core.FONT_HERSHEY_SIMPLEX,1,new Scalar(255,0,0),2);

        //mRGB = inputFrame.rgba();
        return mat1;
        //return null;
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.mimenu,menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        int id = item.getItemId();
        switch (id){
            case R.id.mnuoriginal:
                menu_option = 0;
                break;
            case R.id.menugris:
                menu_option=1;
                break;
            case R.id.menuinversogris:
                menu_option=2;
                break;
            case R.id.menuinvercolor:
                menu_option=3;
                break;
            case R.id.menurojo:
                menu_option=4;
                break;
            case R.id.menuverde:
                menu_option = 5;
                break;
            case R.id.menuazul:
                menu_option=6;
                break;
            case R.id.colorpiel:
                menu_option=7;
                break;
            case R.id.detechoja:
                menu_option=8;
                break;
            case R.id.bordes:
                menu_option=9;
                break;
            case R.id.menurostro:
                menu_option=10;
                break;
            default:
                menu_option = 0;
                break;
        }
        return true;
    }
    private File getCascadeFile(int resId) {
        try {
            InputStream is = getResources().openRawResource(resId);
            File cascadeDir = getDir("cascade", Context.MODE_PRIVATE);
            File mCascadeFile = new File(cascadeDir, "haarcascade_frontalface_alt2.xml");

            FileOutputStream os = new FileOutputStream(mCascadeFile);

            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = is.read(buffer)) != -1) {
                os.write(buffer, 0, bytesRead);
            }
            is.close();
            os.close();

            return mCascadeFile;
        } catch (Exception e) {
            Log.e("MainActivity", "Error loading cascade", e);
            return null;
        }
    }
}
