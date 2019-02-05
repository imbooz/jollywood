// This will find today's date
function calendar() {

	var day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
	var month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
	var d = new Date();
	SetText('calendar-day', day[d.getDay()]);
	SetText('calendar-date', d.getDate());
	SetText('calendar-month-year', month[d.getMonth()]+' '+(1900+d.getYear()));
}

// This will set the text value of <p> tags
function SetText(id, val) {
	if(val < 10){
		val = '0' + val; // leading 0 if val < 10
	}
	var x = document.getElementsByClassName(id);
    for (var i=0; i < x.length; i++){
        x[i].innerHTML = val;
    }
}

// This will do smth with quotes
function quote() {
	var quotes = ['“I have never let my schooling interfere with my education.”',
				  '“Intelligence plus character-that is the goal of true education.”',
				  '“Education is the most powerful weapon which you can use to change the world.”',
				  '“The mind is not a vessel to be filled, but a fire to be kindled.”',
				  '“Our children are only as brilliant as we allow them to be.”',
				  '“Children must be taught how to think, not what to think.”',
				  '“Those who educate children well are more to be honored than they who produce them; for these only gave them life, those the art of living well.”',
				  '“Whatever the cost of our libraries, the price is cheap compared to that of an ignorant nation.”',
				  '“True education does not consist merely in the acquiring of a few facts of science, history, literature, or art, but in the development of character.”',
				  '“The best teacher is not the one who knows most but the one who is most capable of reducing knowledge to that simple compound of the obvious and wonderful.”',
				  '“I am indebted to my father for living, but to my teacher for living well.”',
				  '“The mediocre teacher tells. The good teacher explains. The superior teacher demonstrates. The great teacher inspires.”',
				  '“Live as if you were to die tomorrow. Learn as if you were to live forever.”',
				  '“The mind once enlightened cannot again become dark.”',
				  '“Without education, we are in a horrible and deadly danger of taking educated people seriously.”',
				  '“The task of the modern educator is not to cut down jungles, but to irrigate deserts.”'];

	var authors = ['Mark Twain',
				   'Martin Luther King Jr.',
				   'Nelson Mandela',
				   'Plutarch',
				   'Eric Micha’el Leventhal',
				   'Margaret Mead',
				   'Aristotle',
				   'Walter Cronkite',
				   'David O. McKay',
				   'H.L. Mencken',
				   'Alexander the Great',
				   'William Arthur Ward',
				   'Mahatma Gandhi',
				   'Thomas Paine',
				   'G.K. Chesterton',
				   'C.S. Lewis'];

	var random = Math.floor(Math.random()*quotes.length);

	SetText('quote-text', quotes[random]);
	SetText('quote-author', authors[random]);
}

// Call Calendar() When page loads
$(function(){
	calendar();
	quote();
	$('[data-toggle="tooltip"]').tooltip(); 
});

