package com.example.sistemaexperto.API;

import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.converter.scalars.ScalarsConverterFactory;

public class RetrofiNeurona {
    private static Retrofit salidaRetrofit;

    public static Retrofit getInstance() {
        if (salidaRetrofit == null) {
            salidaRetrofit = new Retrofit.Builder().
                    baseUrl("https://apipy-uni-435755b56d9c.herokuapp.com/")
                    .addConverterFactory(ScalarsConverterFactory.create())
                    .build();
        }
        return salidaRetrofit;
    }
}
