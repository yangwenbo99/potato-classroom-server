$(document).ready(function() {
	/*
    // Instructor view
    $("#question-form").submit(function(event) {
        event.preventDefault();
        const question = $("#question").val();
        const question_type = $("#question_type").val();
        $.post("/post_question", { question: question, question_type: question_type }, function(data) {
            if (data.success) {
                $("#question").val("");
                alert("Question posted successfully!");
            } else {
                alert("Error posting question.");
            }
        });
    });

    $("#show-results").click(function() {
        $.get("/get_results", function(data) {
            if (data.success) {
                $("#results-list").empty();
                data.results.forEach(function(result) {
                    $("#results-list").append(`<li>${result.question}: ${result.answer}</li>`);
                });
            } else {
                alert("Error fetching results.");
            }
        });
    });
*/

    // Student view
    function fetchQuestion() {
        $.get("/get_question", function(data) {
            if (data.success) {
                $("#question").text(data.question);
                $("#question_type").text(data.question_type);
                $("#answer-form").data("question-id", data.question_id);
            } else {
                setTimeout(fetchQuestion, 5000);
            }
        });
    }

    fetchQuestion();
/*
    $("#answer-form").submit(function(event) {
        event.preventDefault();
        const answer = $("#answer").val();
        const question_id = $("#answer-form").data("question-id");
        $.post("/submit_answer", { answer: answer, question_id: question_id }, function(data) {
            if (data.success) {
                $("#answer").val("");
                alert("Answer submitted successfully!");
                fetchQuestion();
            } else {
                alert("Error submitting answer.");
            }
        });
    });
*/
});
