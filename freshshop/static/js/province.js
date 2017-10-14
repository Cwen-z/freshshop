/**
 * Created by python on 17-10-13.
 */
$(function () {
    $.get('/users/pro_id/', function (data) {
        $.each(data.list1, function (index, item) {
            $('#pro').append('<option value="'+item.aid+'">'+item.city+'</option>')
        })
    })
    //查询市的信息
    $('#pro').change(function () {
        //area140000/
        // alert('/users/pro_id/'+$(this).val())
        $.get('/users/pro_id/'+$(this).val(),function (list) {
            city=$('#city');
            city.empty().append('<option value="0">请选择市</option>')
            $('#dis').empty().append('<option value="0">请选择区县</option>')
            //{data:[{id:1,title:北京},{id:2,title:天津},...]}
            $.each(list.list1,function (index, item) {
                //{id:1,title:北京}
                city.append('<option value="'+item.aid+'">'+item.city+'</option>');
            });
        });
    });

    //查询区县的信息
    $('#city').change(function () {
        $.get('/users/pro_id/'+$(this).val(),function (list) {
            dis=$('#dis').empty().append('<option value="0">请选择区县</option>');
            $.each(list.list1,function (index, item) {
               dis.append('<option value="'+item.aid+'">'+item.city+'</option>');
            });
        });
    });
    var error_phone = true
    var error_message = true
    function check() {
        var user1 = $('#user').val()
        var pro1 = $('#pro').val()
        var city1 = $('#city').val()
        var dis1 = $('#dis').val()
        var site = $('.site_area').val()
        var pc = $('#pc').val()
        val = $('#phone').val();
        reg = /^1\d{10}$/;
        if(reg.test(val)){
            $('#phone').next().hide()
            error_phone = false
        }
        else{
            $('#phone').next().show()
            error_phone = true
        }
        if (user1=='' || site=='' || pc=='')
        {
            $('#empty').html("以上选项皆不能为空").show()
            error_message = true
        }
        else
        {
            if (pro1==0 && city1==0 && dis1==0)
            {
                $('#empty').html("以上选项皆不能为空").show()
                error_message = true
            }
            else
            {
                $('.info_submit').next('span').hide()
                error_message = false
            }
        }
    }
    $('#phone').blur(function() {
        check()
    })
    $('#phone').focus(function () {
        $('#phone').next().hide()
    })
    $('#user').focus(function () {
        $('.info_submit').next('span').hide()
    })
    $('#pro').focus(function () {
        $('.info_submit').next('span').hide()
    })
    $('#city').focus(function () {
        $('.info_submit').next('span').hide()
    })
    $('#dis').focus(function () {
        $('.info_submit').next('span').hide()
    })
    $('#pc').focus(function () {
        $('.info_submit').next('span').hide()
    })
    $('.site_area').focus(function () {
        $('.info_submit').next('span').hide()
    })
    $('form').submit(function () {
        check()
        console.log(error_phone)
        if (error_phone==false && error_message==false)
        {
            return true
        }
        else
        {
            return false
        }
    })
        $('.edits').click(function () {
            var aid = $(this).next().html()
            $.post('/users/editor/'+aid,function (data) {
            list2 = data.list1
            dict1 = list2[0]
            $('#user').val(dict1.shoujian)
            $('#pro').val(dict1.pro_id)
            $.get('/users/pro_id/'+dict1.pro_id,function (list) {
                city=$('#city');
                city.empty().append('<option value="0">请选择市</option>')
                $('#dis').empty().append('<option value="0">请选择区县</option>')
                //{data:[{id:1,title:北京},{id:2,title:天津},...]}
                $.each(list.list1,function (index, item) {
                    //{id:1,title:北京}
                    city.append('<option value="'+item.aid+'">'+item.city+'</option>');
                });
            })
            $('#city').val(dict1.city_id)
            $('.site_area').val(dict1.det)
            $('#pc').val(dict1.pc)
            $('#phone').val(dict1.phone)

            $('form').attr('action','/users/address_handler/'+aid)

        })
    })
})