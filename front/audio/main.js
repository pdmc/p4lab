            var recorder;  
            var audio = document.querySelector('audio');  
              
            function startRecording() {
            	
                $(".contrs>div:nth-child(2n)").css({"display":"inline-block"});
                $(".contrs>div:first-of-type").css({"display":"none"});  
      
               if(recorder){
                   recorder.start();
                   return;  
               }
               
                HZRecorder.get(function (rec) {  
                    recorder = rec;  
                    recorder.start();  
                },{error:showError}); 
                 
            }  
            function request(url,opt){
                const options = { mode: 'cors'};
                if (opt) {
                    for (var key in opt) {
                        options[key] = opt[key]
                    }
                }
                if (options.method === "POST") {
                    const formData = new FormData();
                    const data = options.body;
                    for (var key in data){formData.append(key,data[key])}
                    options.body = formData;
                }
                return fetch(url,options).then(function (res) {
                    console.log(res);
                    // return res;
                     if (res.status !== 200) {
                         console.log('Looks like there was a problem. Status Code: ' + res.status);
                         return;
                     }
            
                    // // 处理响应中的文本信息 
                     res.json().then(function(data) {
//                       console.log(data);
                         var yuyin ="https://dmc.pk4yo.com/tts/"+data.text+".mp3";
                         var oldHtml = $(".btjumbotron").html();
                         var newHtml = oldHtml +'<div class="leftd"><div class=" speech left"><img class="laba_img" src="../images/laba.png" /><audio class="au" controls  src='+yuyin+'></audio></div></div>'
//                       var newHtml = oldHtml +'<div class="leftd"><div class=" speech left"><audio class="au" controls  src='+yuyin+'></audio></div></div>'
//                       var newHtml = oldHtml +'<div class="leftd"><div class="speech left">'+data["text"]+'</div></div>'
                         $(".btjumbotron").html(newHtml);

					var second = ""
					

					
					$(".leftd").bind("click",function(){
//							console.log($(this).children(".left").children(".au"));
							var player = $(this).children(".left").children(".au")[0];
						    var img =  $(this).children(".left").children("img");
						    second = player.duration
							if (player.paused){ /*如果已经暂停*/							
						            player.play(); /*播放*/
						            console.log(img)
						            img.addClass("playing");
								    setTimeout(function(){ 
						               img.removeClass("playing");
						            },second*1000)
						        }else {
						            player.pause();/*暂停*/
						            img.removeClass("playing");
						        }

					})

					
				

	
                     });              
                })
            }                
            function obtainRecord(){  
                 if(!recorder){
                    showError("请先录音");
                    return;
                }
               var record = recorder.getBlob(); 
               console.log(record); 
               if(record.duration!==0){
               downloadRecord(record.blob);
               }else{
                   showError("请先录音")
               }
            };  

            function downloadRecord(record){
              var save_link = document.createElementNS('http://www.w3.org/1999/xhtml', 'a')
                save_link.href = URL.createObjectURL(record);
                var now=new Date;
                save_link.download = now.Format("yyyyMMddhhmmss");
                fake_click(save_link);
            }

       
            function fake_click(obj) {
                var ev = document.createEvent('MouseEvents');
                ev.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                obj.dispatchEvent(ev);
            }

            function getStr(){
              var now=new Date;
              var str= now.toDateString();
            }

            function stopRecord(){  
            	
                recorder&&recorder.stop();  
                $(".contrs>div:nth-child(2n)").css({"display":"none"});
                $(".contrs>div:first-of-type").css({"display":"inline-block"});
            };  
            var msg={};
            //发送音频片段
            var msgId=1;
            function send(){ 
            	
                if(!recorder|| recorder.getBlob().duration <= 0){
                    showError("请先录音");
                    return;
                }
               var data = recorder.getBlob(); 
                msg[msgId]=data;                
                recorder.clear();
                console.log(data.blob);
                var dur=data.duration/10;
                var str="<div class='warper'><div id="+msgId+" class='voiceItem'>"+dur+"s</div></div>"
                $(".messages").append(str);
                msgId++;
                 request("https://dmc.pk4yo.com:8083/travelv",{
                        method: "POST",
                        body: {file:data.blob}
                    })
                 
                   
            }
            
            $(document).on("click",".voiceItem",function(){
                var id=$(this)[0].id;
                var data=msg[id];
                playRecord(data.blob);
            })
            var ct;
            function showError(msg){
                $(".error").html(msg);
                clearTimeout(ct);
                ct=setTimeout(function() {
                    $(".error").html("")
                }, 3000);
            }


            function playRecord(blob){  
                if(!recorder){
                    showError("请先录音");
                    return;
                }
                 recorder.play(audio,blob);  
            };  
              
            // // /* 视频 */  
            // function scamera() {  
            //     var videoElement = document.getElementById('video1');  
            //     var canvasObj = document.getElementById('canvas1');  
            //     var context1 = canvasObj.getContext('2d');  
            //     context1.fillStyle = "#ffffff";  
            //     context1.fillRect(0, 0, 320, 240);  
            //     context1.drawImage(videoElement, 0, 0, 320, 240);  
            // };  
              
            // function playVideo(){  
            //     var videoElement1 = document.getElementById('video1');  
            //     var videoElement2 = document.getElementById('video2');  
            //     videoElement2.setAttribute("src", videoElement1);  
            // };  
