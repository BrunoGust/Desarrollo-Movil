package com.example.sistemaexperto;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import com.example.sistemaexperto.API.RedNeuronal;
import com.example.sistemaexperto.API.RetrofiNeurona;


import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

public class MainActivity extends AppCompatActivity {

    Switch switch1,switch2,switch3,switch4,switch5,switch6,switch7,switch8;
    TextView textViewEn;
    Button btnVeri;
    int x1,x2,x3,x4,x5,x6,x7,x8;
    String url="",result = "";
    RedNeuronal neurona;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        switch1 = (Switch) findViewById(R.id.switch1);
        switch2 = (Switch) findViewById(R.id.switch2);
        switch3 = (Switch) findViewById(R.id.switch3);
        switch4 = (Switch) findViewById(R.id.switch4);
        switch5 = (Switch) findViewById(R.id.switch5);
        switch6 = (Switch) findViewById(R.id.switch6);
        switch7 = (Switch) findViewById(R.id.switch7);
        switch8 = (Switch) findViewById(R.id.switch8);
        textViewEn = (TextView) findViewById(R.id.textViewEnfermedad);
        btnVeri = (Button)findViewById(R.id.btnVerificar);

        btnVeri.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Retrofit retrofit = RetrofiNeurona.getInstance();
                neurona = retrofit.create(RedNeuronal.class);
                x1 = switch1.isChecked() ? 1:0;
                x2 = switch2.isChecked() ? 1:0;
                x3 = switch3.isChecked() ? 1:0;
                x4 = switch4.isChecked() ? 1:0;
                x5 = switch5.isChecked() ? 1:0;
                x6 = switch6.isChecked() ? 1:0;
                x7 = switch7.isChecked() ? 1:0;
                x8 = switch8.isChecked() ? 1:0;
                try {
                    Call<ResponseBody> call = neurona.getEnfermedad(x1, x2, x3, x4, x5, x6, x7, x8);
                    call.enqueue(new Callback<ResponseBody>(){
                        @Override
                        public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                            if (!response.isSuccessful())
                                return;
                            try {
                                result = response.body().string();
                                textViewEn.setText(result);
                            } catch (Exception e) {
                                Toast.makeText(MainActivity.this, e.toString(), Toast.LENGTH_SHORT).show();
                            }
                        }

                        @Override
                        public void onFailure(Call call, Throwable t) {
                            Toast.makeText(MainActivity.this, t.getMessage(), Toast.LENGTH_SHORT).show();
                        }
                    });
                }
                catch (Exception e){
                    Toast.makeText(MainActivity.this, e.toString(), Toast.LENGTH_SHORT).show();
                }

            }
        });

    }



}