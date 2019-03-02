var correct_answers = 0;
var mistakes = 0;
var unanswered = 50;

$(function() {
  
  //// On click of Start button the view changes!
  $("#start-test").click(function(){
    // Change of a view
    $(".alerter").toggle();
    $("#test-area").toggle();

    if($(this).text() == " Start"){
      
      $(this).text(" Stop");
      $(this).toggleClass('btn-outline-primary btn-outline-danger');
    
    } else if ($(this).text() == " Stop" ) {

      $(this).text(" Review");
      $(this).toggleClass('btn-outline-danger btn-outline-info');
      $("#test-area input, #test-area button").prop('disabled', true);
      $("#result .unanswered").text(unanswered);
      $("#result .correct").text(correct_answers);
      $("#result .incorrect").text(mistakes);

      // Check Correct answers and decide on the level of students
      if( correct_answers >= 0) {
        $("#result .level").text("Beginner")
      } else if (correct_answers > 15) {
        $("#result .level").text("Elementary")
      } else if (correct_answers > 24) {
        $("#result .level").text("Pre-Intermediate")
      } else if (correct_answers > 32) {
        $("#result .level").text("Intermediate")
      } else if (correct_answers > 39) {
        $("#result .level").text("Upper-Intermediate")
      } else if (correct_answers > 45) {
        $("#result .level").text("Advanced")
      }
    
    } else if($(this).text() == " Review") {

      $(this).text(" Hide");
      $(this).toggleClass('btn-outline-info btn-outline-warning');
    
    } else {
    
      $(this).text(" Review");
      $(this).toggleClass('btn-outline-info btn-outline-warning');
    
    }

    // Timer






    //// Test
    $(".q").click(function(){

      //Get the answer into variable
      answer = $(this).attr('data-answer');

      //Check if answer is correct then success
      if (answer == 'correct') {

        $(this).toggleClass('btn-outline-info btn-success');
        $(this).parent().children().prop('disabled', true);
        correct_answers++;
        unanswered--;
        $("#result .correct").text(correct_answers);

      } else { // If not correct then danger

        $(this).toggleClass('btn-outline-info btn-danger');
        $(this).parent().children().prop('disabled', true);
        mistakes++;
        unanswered--;
        $("#result .incorrect").text(mistakes);

      }

    });

  });



}); // End of jQuery