package com.example.appcalculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.text.DecimalFormat;

public class MainActivity extends AppCompatActivity {
    EditText inputn1, inputn2;
    Button btnSumar, btnRes, btnMul, btnDiv;
    float n1,n2,resultado = 0;
    String mensaje ="";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        DecimalFormat df = new DecimalFormat("#.###");

        inputn1 = (EditText) findViewById(R.id.inputn1);
        inputn2 = (EditText) findViewById(R.id.inputn2);

        btnSumar = (Button) findViewById(R.id.btnSumar);
        btnRes = (Button) findViewById(R.id.btnRes);
        btnMul = (Button) findViewById(R.id.btnMul);
        btnDiv = (Button) findViewById(R.id.btnDiv);

        //Funcion suma
        btnSumar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                n1 = Float.valueOf(inputn1.getText().toString());
                n2 = Float.valueOf(inputn2.getText().toString());
                resultado = n1 + n2;
                mensaje = "El resultado de la suma es : "+ df.format(resultado);
                Toast.makeText(getApplicationContext(),mensaje,Toast.LENGTH_LONG).show();
            }
        });
        btnRes.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                n1 = Float.valueOf(inputn1.getText().toString());
                n2 = Float.valueOf(inputn2.getText().toString());
                resultado = n1 - n2;
                mensaje = "El resultado de la resta es : "+ df.format(resultado);
                Toast.makeText(getApplicationContext(),mensaje,Toast.LENGTH_LONG).show();
            }
        });

        btnMul.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                n1 = Float.valueOf(inputn1.getText().toString());
                n2 = Float.valueOf(inputn2.getText().toString());
                resultado = n1 * n2;
                mensaje = "El resultado de la multiplicacion es : "+ df.format(resultado);
                Toast.makeText(getApplicationContext(),mensaje,Toast.LENGTH_LONG).show();
            }
        });

        btnDiv.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                n1 = Float.valueOf(inputn1.getText().toString());
                n2 = Float.valueOf(inputn2.getText().toString());
                if (n2 == 0){
                    mensaje = "Error! No se puede dividir entre 0.";
                }
                else{
                    resultado = n1 / n2;
                    mensaje = "El resultado de la division es: "+ df.format(resultado);
                }

                Toast.makeText(getApplicationContext(),mensaje,Toast.LENGTH_LONG).show();
            }
        });

    }
}