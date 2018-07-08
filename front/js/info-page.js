/*!
 * Date: 2017-03-20T18:59Z
 */

function hello()
{
  alert("Hello World!");
}




// ---------------------------------------  FrontPage  ----------------------------------------








// ---------------------------------------  InfoPage  ----------------------------------------
$(document).ready(function(){
	$("#intro-pro").on("click", function() {
		$("#intro-pro span").html(parseInt($("#intro-pro span").html())+1);
	});
	$("#intro-fav").on("click", function() {
		//$("#intro-fav span").html(parseInt($("#intro-fav span").html())+1);
		label = $("#intro-fav span").html()
		if(label == "收了"){
			$("#intro-fav").css("background","url(../images/favorite-ok.png) no-repeat 5px 5px");
			$("#intro-fav").css("background-size","30px 30px");	/* 去掉一切绝对值 */
			$("#intro-fav").css("background-color","white");	/* 纯粹为了图片的白色背景 */
			$("#intro-fav span").html("已收");
		}else{
			$("#intro-fav").css("background","url(../images/favorite.png) no-repeat 5px 5px");
			$("#intro-fav").css("background-size","30px 30px");
			$("#intro-fav").css("background-color","white");
			$("#intro-fav span").html("收了");
		}
	});
});




