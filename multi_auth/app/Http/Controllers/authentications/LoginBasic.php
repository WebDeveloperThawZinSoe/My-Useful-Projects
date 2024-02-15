<?php

namespace App\Http\Controllers\authentications;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;

class LoginBasic extends Controller
{
  public function index()
  {
    return view('content.authentications.auth-login-basic');
  }


  //Login
  public function Login(Request $request){
      $validator = Validator::make($request->all(), [
          'email' => 'required|email',
          'password' => 'required',
      ]);

      if ($validator->fails()) {
          return redirect()->route('auth-login-basic')
              ->withErrors($validator)
              ->withInput();
      }

      // Attempt to log in the user
      $credentials = $request->only('email', 'password');

      if (Auth::attempt($credentials)) {
          // Authentication passed
          $user_role = Auth::user()->role;
          if($user_role == 1){
            return redirect("/super-admin");
          }else if($user_role == 2){
              return redirect("/admin");
          }else if($user_role == 3){
              return redirect("/shop-owner");
          }else if($user_role == 4){
              return redirect("/shop-manager");
          }else if($user_role == 5){
              return redirect("/customer");
          }else{
              return redirect("/auth/login-basic");
          }
      }

      // Authentication failed
      return redirect()->route('auth-login-basic')
          ->with('error', 'Invalid email or password')
          ->withInput();
  }
}
