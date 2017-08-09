<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class Demo extends Controller
{
    public function demo1()
    {  
    	$data=DB::table('study1')->paginate(15);
    	return view('demo1',['data'=>$data]);
    }
    public function demo2(Request $request)
    {
        //$data=$request->all();
        $ddd=$request->only(['name','age','class']);
        //var_dump($ddd);

       //die;
        // $bool=DB::table('study1')->insert(
        // 	[
	       //  	'name'=>$data['name'],
	       //  	'age'=>$data['age'],
	       //  	'class'=>$data['class']
        // 	]
        // 	);


        $bool=DB::table('study1')->insert($ddd);
        var_dump($bool);
    }
    public function demo3(Request $request ,$id='')
    {
        if($request->isMethod('get')){
        	  $data=DB::table('study1')->where(['id'=>$id])->first();
             return view('demo3',['data'=>$data]);
        }else{
            $data=$request->only(['name','age','class','relish','sex']); 
             $id=$request->input('id'); 
             $bool=DB::table('study1')->where(['id'=>$id])->update($data);
             if($bool){
                 return redirect()->action('Demo@demo1');
             }
        } 

    }
    public function demo4($id='')
    {
        $data=DB::table('study1')->where(['id'=>$id])->first();
        dd($data);
    }
}
