/*!
 * Date: 2017-03-20T18:59Z
 */

function hello()
{
  alert("Hello World!");
}

POST_DOMAIN = "dmc.pk4yo.com";

// ---------------------------------------  FrontPage  ----------------------------------------



// some  一些中文




// ---------------------------------------  IntroPage  ----------------------------------------
var firstopen = 1;
$(document).ready($(function(){
	//alert("ready");
	$("#nbarticle").on('click', function () { 
		if(firstopen == 1){
			location.href = "article.html";
			firstopen = 0;
			return false;
		}else{
			return true;
		}
	});/**/

}))



