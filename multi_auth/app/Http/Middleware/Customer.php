<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;
use Auth;
class Customer
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        if (!Auth::check()) {
            return redirect("/auth/login-basic");
        }
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
            return $next($request);
        }else{
            return redirect("/auth/login-basic");
        }
    }
}
