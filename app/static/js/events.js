// https://stackoverflow.com/questions/4588759/how-do-you-set-a-javascript-onclick-event-to-a-class-with-css
// This jQuery snippet only apply to divs with a specific class:
$(document).ready(function() {
        $('div.event').click(function() {
            alert('ho ho ho');
        });
    });





//https://stackoverflow.com/questions/4002671/how-to-clone-content-of-a-div-to-another-div
//You can add a class on click (or other event) that is the hard coded to clone. In this example there is a list
// of same class names containing styled content (divs etc) - add the .CloneMe class but first remove that class
// to empty the div in case the user selects a different item. )to be safe remove any html as well. Then apply
// the class using (this) to avoid grabbing all of the items with that class name and finally append to the div.
// The result is the user can select any item with that class name and populate it in the container.
// - I imagine using a class for the container would allow you to populate it in more than one place.
$(".from").click(function () {
     $(".from").removeClass("CloneMe");
     $("#to").html('');
     $(this).addClass("CloneMe");
     $(".CloneMe").clone().appendTo("#container priority");
     //How do I prevent the user to append it to a schedule with some or all of the time slots occupied?
});

//Or this:
$("#from").clone().appendTo($("#to"));

//But it will not remove/hide the main DIV. To hide the main div, do this:
$("#from").clone().appendTo($("#to"));
$("#from").remove();




function copyToPersonalSchedule() {

}