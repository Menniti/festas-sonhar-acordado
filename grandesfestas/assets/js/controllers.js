(function(angular){
    var app = angular.module('sonhar.controllers', []);

    app.controller('SubscriptionInfoCtrl', [
        '$scope', '$location', 'Volunteer', 'Subscription', 'pipe',
        function($scope, $location, Volunteer, Subscription, pipe){
            var volunteer = new Volunteer();
            var subscription = new Subscription();

            $scope.volunteer = volunteer;
            $scope.subscription = subscription;

            $scope.recover_subscription_id = function(){
                if(!volunteer.email) return;

                Volunteer.query({'email': volunteer.email}).$promise
                    .then(function(results){
                        volunteer.id = results.length === 1 ? results[0].id : undefined;
                        return Subscription.query({'volunteer': volunteer.id}).$promise;
                    })
                    .then(function(results){
                        subscription.id = results.length === 1 ? results[0].id : undefined;
                    });
            };

            $scope.save = function() {
                var promise = volunteer.id ? volunteer.$update() : volunteer.$save();

                promise.then(function(){
                    subscription.volunteer = volunteer.id;
                    pipe.volunteer = volunteer;
                    pipe.subscription = subscription;
                    $location.path('/inscricao/treinamento');
                });
            };
        }
    ]);

    app.controller('SubscriptionTrainingCtrl', ['$scope', 'Training', 'Subscription', 'pipe',
        function($scope, Training, pipe) {
            var training_list = [];
            $scope.training_list = training_list;

            Training.query(function(list){
                training_list = list;
                $scope.training_list = training_list;
            });
        }
    ]);
})(angular);
