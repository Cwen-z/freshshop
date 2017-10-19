$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;
    var error_phone = false

	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#user_name').focus(function() {
		$(this).next().hide();
	});


	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#pwd').focus(function() {
		$(this).next().hide();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#cpwd').focus(function() {
		$(this).next().hide();
	});

	$('#email').blur(function() {
		check_email();
	});

	$('#email').focus(function() {
		$(this).next().hide();
	});
	$('#phone').blur(function() {
		check_phone();
	});

	$('#phone').focus(function() {
		$(this).next().hide();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('大人，请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		//数字字母或下划线
		var reg = /^[a-zA-Z0-9_]{5,20}$/;
		var val = $('#user_name').val();

		if(val==''){
			$('#user_name').next().html('大人，用户名不能为空！')
			$('#user_name').next().show();
			error_name = true;
			return;
		}

		if(reg.test(val))
		{
            $.get('/users/register_exist/?name='+$('#user_name').val(),function (data) {
                list = data.count
                if(list[0].user_num != 0){
                    $('#user_name').next().html("用户名被注册了，换换").show()
                    error_name = true;
                    }
                else{

                    $('#user_name').next().hide();
			        error_name = false;
                    }
                })
		}
		else
		{
			$('#user_name').next().html('大人，用户名是5到20个英文、数字和“_”的组合')
			$('#user_name').next().show();
			error_name = true;
		}

	}


	function check_pwd(){
		var reg = /^[\@A-Za-z0-9\!\#\$\%\^\&\*\.\~]{6,20}$/;
		var val = $('#pwd').val();

		if(val==''){
			$('#pwd').next().html('大人，密码不能为空！')
			$('#pwd').next().show();
			error_password = true;
			return;
		}

		if(reg.test(val))
		{
			$('#pwd').next().hide();
			error_password = false;
		}
		else
		{
			$('#pwd').next().html('大人，密码是6到20位字母、数字、特殊字符的组合')
			$('#pwd').next().show();
			error_password = true;
		}
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('大人，密码不一致，再瞧瞧')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}

	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;
		var val = $('#email').val();

		if(val==''){
			$('#email').next().html('大人，邮箱不能为空！')
			$('#email').next().show();
			error_email = true;
			return;
		}

		if(re.test(val))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('大人，邮箱格式不正确')
			$('#email').next().show();
			error_email = true;
		}

	}

	function check_phone(){
		var re = /^1\d{10}$/;
		var val = $('#phone').val();

		if(val==''){
			$('#phone').next().html('大人，号码不能为空！')
			$('#phone').next().show();
			error_email = true;
			return;
		}

		if(re.test(val))
		{
		    $.get('/users/register_exist/?phone='+$('#phone').val(),function (data) {
		        list = data.count
                if(list[0].user_phone==1){
                    $('#phone').next().html("号码被注册啦，换个吧").show()
                    error_password = true;
                    }
                else{

                    $('#phone').next().hide();
			        error_phone = false;
                    }
                })

		}
		else
		{
			$('#phone').next().html('手机号码为1开头，11位数字组合')
			$('#phone').next().show();
			error_phone = true;
		}

	}


	$('.reg_form').submit(function() {
		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false && error_phone == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});
})