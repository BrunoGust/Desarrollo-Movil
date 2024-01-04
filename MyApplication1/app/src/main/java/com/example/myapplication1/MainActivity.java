package com.example.myapplication1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    TextView lblmensaje;
    Button button;

    int contador = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        lblmensaje = (TextView) findViewById(R.id.lblmensaje);
        button = (Button) findViewById((R.id.button));
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String mensaje = "Hola mundo cruel " + (++contador);
                lblmensaje.setText(mensaje);
                Toast.makeText(getApplicationContext(),mensaje, Toast.LENGTH_LONG).show();
            }
        });
    }
}