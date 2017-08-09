<?php

namespace App\Http\Middleware;

use Closure;

class CheckAge
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {    
         
        if( $request->age<=200)
        {
            return redirect('bbb/fff1');
        }else{
            return redirect('bbb/fff2');
        }

        return $next($request);
    }

}
