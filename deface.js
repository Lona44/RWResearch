function getAllElementsWithAttribute(attribute)
{
  var matchingElements = [];
  
  var allElements = document.getElementsByTagName('span');
  
  for (var i = 0, n = allElements.length; i < n; i++)
  {
    if (allElements[i].getAttribute(attribute))
    {
      matchingElements.push(allElements[i]);
    }
  }
  return matchingElements;
}

var terminalElements = getAllElementsWithAttribute("terminal");

function terminals_init()
{
  var elements = terminalElements;
  for (var i = 0; i < elements.length; i++)
  {
    var e = elements[i]
    e.completeHTML = e.innerHTML
    e.innerHTML = ""
    e.i = 0
  }

}

function terminals_start()
{
  //terminalIntervalFunction = function(){ terminals_next() }
  //setInterval(terminalIntervalFunction, 1000/60);
  terminals_next()
}

function terminals_next()
{
  var done = true
  var elements = terminalElements;

  for (var i = 0; i < elements.length && done == true; i++)
  {
    var e = elements[i]

    e.i ++

    if (e.innerHTML.length >= e.completeHTML.length)
    {
      e.innerHTML = e.completeHTML
    }
    else
    {
      var s =  e.completeHTML.substring(0, e.i) 

      if (s.slice(-1) == " ") 
      {
        if(e.innerHTML.length % 6 == 0 ) { s = s + "" } else { s = s + "|" }
      }
      else
      {
        s = s + "|"
      }

      e.innerHTML = s
      e.parentNode.style.display = 'none'
      e.parentNode.style.display = 'block'
      done = false
    }
  }

  if (!done)
  {
    //window.clearInterval(terminalIntervalFunction)
    setTimeout(terminals_next, 800/20)
  }
}

terminals_init()

window.onload = function() { terminals_start() };





(function () {
  const second = 1000,
        minute = second * 60,
        hour = minute * 60,
        day = hour * 24;

  let birthday = "Jun 18, 2021 00:00:00",
      countDown = new Date(birthday).getTime(),
      x = setInterval(function() {

        let now = new Date().getTime(),
            distance = countDown - now;

        document.getElementById("days").innerText = Math.floor(distance / (day)),
          document.getElementById("hours").innerText = Math.floor((distance % (day)) / (hour)),
          document.getElementById("minutes").innerText = Math.floor((distance % (hour)) / (minute)),
          document.getElementById("seconds").innerText = Math.floor((distance % (minute)) / second);

        //do something later when date is reached
        if (distance < 0) {
          let headline = document.getElementById("headline"),
              countdown = document.getElementById("countdown"),
              content = document.getElementById("content");

          headline.innerText = "Time's up!";
          countdown.style.display = "none";
          content.style.display = "block";

          clearInterval(x);
        }
        //seconds
      }, 0)
  }());
