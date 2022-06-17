$('#comment').on("keyup",function(){
   var count = $('#comment').val().trim().split(' ');
  $('#wordCount').text(count.length);
});   