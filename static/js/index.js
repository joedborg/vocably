$(function () {
    function ViewModel() {
        var self = this;
        self.finished = ko.observable(false);
        self.questionID = ko.observable();
        self.questionViewing = ko.observable();
        self.questionAnswer = ko.observable();
        self.questions = ko.observableArray();
        self.numberCorrect = ko.observable(0);
        self.numberAnswered = ko.pureComputed(function () {
            return self.questionID() + 1
        });

        self.questionID.subscribe(function (newVal) {
            self.questionViewing(
                ko.mapping.fromJS(
                    self.questions()[newVal]
                )
            );
        });

        self.questionAnswer.subscribe(function (newVal) {
            if (newVal) {
                $.post('answer', {answer: newVal, question: self.questionID}, function (response) {
                    if (response['correct'] == true) {
                        self.numberCorrect(self.numberCorrect() + 1);
                    }
                    if (self.questionID() + 1 == self.questions().length) {
                        self.finished(true);
                    } else {
                        self.questionID(self.questionID() + 1);
                        self.questionAnswer(undefined);
                    }
                })
            }
        });

        $.getJSON('questions', function (response) {
            self.questions(response);
            self.questionID(0);
        });
    }

    ko.applyBindings(new ViewModel());
});