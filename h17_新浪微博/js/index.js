$(function () {
   // 1 监听内容的时时输入（只有有输入时，“发布”才能点击）
   //  change:只有当失去焦点时，才会触发，所以时时监听不行
   // $(".comment").change(function () {
   //     console.log($(this).val());
   // });
   //  需要使用事件委托
    // 在入口函数加载之前就执行的元素，可以委托给body
    $("body").delegate(".comment", "propertychange input", function () {
        // console.log($(this).val());
        // 判断是否输入了内容
        if($(this).val().length > 0){
            // 让按钮可用
            // 返回true，false用prop，否则用attr
            $(".send").prop("disabled", false);
        }else{
            // 让按钮不可用
            $(".send").prop("disabled", true);
        }
    });
    // 1 监听发布按钮的点击
   $(".send").click(function () {
       // alert("send");
       // 拿到输入的内容
       var $text = $(".comment").val();
       // 根据内容创建节点
       var $weibo = createEle($text);
       // 插入微博:把新微博插入到最前面prepend
       $(".messageList").prepend($weibo);
       // 清空textarea
       //$(".comment").val();
       $(".comment").val('');
       $(".send").prop("disabled", true);
   });
   // 2-4 由于“微博”是动态创建的，所以对应按钮的监听只能用委托函数
   // 2 监听顶点击
   $("body").delegate(".infoTop", "click", function () {
       $(this).text(parseInt($(this).text())+1);
   });
   // 3 监听踩点击
    $("body").delegate(".infoDown", "click", function () {
        $(this).text(parseInt($(this).text())+1);
    });
   // 4 监听删除点击
    $("body").delegate(".infoDel", "click", function () {
        $(this).parents(".info").remove();
    });

   // 创建节点方法
    function createEle(text) {
        var $weibo = $("        <div class=\"info\">\n" +
            "            <p class=\"infoText\">"+text+"</p>\n" +
            "            <p class=\"infoOperation\">\n" +
            "                <span class=\"infoTime\">"+formatDate()+"</span>\n" +
            "                <span class=\"infoHandle\">\n" +
            "                    <a href=\"javascript:;\" class='infoTop'>0</a>\n" +
            "                    <a href=\"javascript:;\" class='infoDown'>0</a>\n" +
            "                    <a href=\"javascript:;\" class='infoDel'>删除</a>\n" +
            "                </span>\n" +
            "            </p>\n" +
            "        </div>")
        return $weibo;
    }

    // 创建时间方法
    function formatDate() {
        var $date = new Date();
        // 2018-4-3 15:36:28
        var $arr = [$date.getFullYear()+'-',
        addZero($date.getMonth()+1)+'-',
        addZero($date.getDate())+' ',
        addZero($date.getHours())+':',
        addZero($date.getMinutes())+':',
        addZero($date.getSeconds())];
        return $arr.join("", $arr);
    };
	
	// 不够10补0
	function addZero(obj) {
		if(obj < 10){
			return '0'+obj;
		}else{
			return obj;
		}
	};
});
