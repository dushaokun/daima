@include('header')
<form action="{{url('demo3')}}" method="post">
	 <input type="hidden" name="_token" value="{{csrf_token()}}">
	 <input type="hidden" name="id" value="{{$data->id}}">
	 <input type="text" name="name" value="{{$data->name}}">名字<br/>
	 <input type="text" name="age" value="{{$data->age}}">年龄<br/>
	 <input type="text" name="class" value="{{$data->class}}">班级<br/>
	 <input type="text" name="sex" value="{{$data->sex}}">性别<br/>
	 <input type="text" name="relish" value="{{$data->relish}}">爱好<br/>
	 <input type="submit" value="修改">
</form>