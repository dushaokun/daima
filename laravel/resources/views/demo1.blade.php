@include('header')
<body>
	  <form action="{{url('demo2')}}" method="post">
	  	  <input type="hidden" name="_token" value="{{csrf_token()}}">
          <input type="text" name="name" >姓名<br/>
          <input type="text" name="age">年龄<br/>
          <input type="text" name="class">班级<br/>
          <input type="submit" value="添加">
	  </form>


	  <table  style="text-align:center; border: 1px solid " border="1px">
	  	   <tr> 
              <th width="5%">姓名</th>
              <th width="5%">年龄</th>
              <th width="5%">班级</th>
              <th width="5%">操作</th>
	  	   </tr>
	  	   
	  	   @foreach($data as $value)
	  	   <tr>
	  	   	  <td><a href="{{url('demo4',['id'=>$value->id])}}">{{$value->name}}</a></td>
	  	   	  <td>{{$value->age}}</td>
	  	   	  <td>{{$value->class}}</td>
	  	   	  <td><a href="{{url('demo3',['id'=>$value->id])}}">修改</a></td>
	  	   	</tr>
	  	   @endforeach
	   
        
	  </table>
	   {{$data->links()}}
</body>
</html>