(function(angular){
    var app = angular.module('sonhar.controllers', []);

    app.controller('SubscriptionInfoCtrl', [
        '$scope', '$location', '$timeout', 'Volunteer', 'Subscription', 'pipe',
        function($scope, $location, $timeout, Volunteer, Subscription, pipe){
            window.Volunteer = Volunteer;

            $scope.volunteer = pipe.volunteer || new Volunteer();
            $scope.subscription = pipe.subscription || new Subscription();

            function recover_id(){
                var query = {'email': $scope.volunteer.email};
                Volunteer.query(query, function(results){
                    $scope.volunteer.id = results.length === 1 ? results[0].id : undefined;
                });
            }

            var recover_timeout_id = null;
            $scope.$watch('volunteer.email', function debounced(before, now){
                if(before === now || now === '') { return; }

                if(recover_timeout_id) {
                    $timeout.cancel(recover_timeout_id);
                }

                $timeout(recover_id, 500);
            });

            $scope.save = function() {
                $scope.volunteer.save().then(function(){
                    pipe.volunteer = $scope.volunteer;
                    pipe.subscription = $scope.subscription;
                    $location.path('/inscricao/treinamento');
                });
            };
        }
    ]);

    app.controller('SubscriptionTrainingCtrl', ['$scope', '$location', 'Training', 'pipe',
        function($scope, $location, Training, pipe) {
            var training_list = [];
            $scope.training_list = training_list;
            $scope.subscription = pipe.subscription;

            Training.query(function(list){
                training_list = list;
                $scope.training_list = training_list;
            });

            $scope.save = function() {
                var promise = $scope.subscription.id ? $scope.subscription.$update() : $scope.subscription.$save();

                promise.then(function(){
                    $location.path('/inscricao/pagamento');
                });
            };
        }
    ]);

    app.controller('SubscriptionTrainingCtrl', ['$scope', '$location', 'Training', 'pipe',
        function($scope, $location, Training, pipe) {
            var training_list = [];
            $scope.training_list = training_list;
            $scope.subscription = pipe.subscription;

            Training.query(function(list){
                training_list = list;
                $scope.training_list = training_list;
            });

            $scope.save = function() {
                var promise = $scope.subscription.id ? $scope.subscription.$update() : $scope.subscription.$save();

                promise.then(function(){
                    $location.path('/inscricao/pagamento');
                });
            };
        }
    ]);

    app.controller('SubscriptionPaymentCtrl', ['$scope', '$location', 'pipe',
        function($scope, $location, pipe) {
            $scope.subscription = pipe.subscription;

            $scope.save = function() {
                var promise = $scope.subscription.id ? $scope.subscription.$update() : $scope.subscription.$save();

                promise.then(function(){
                    $location.path('/inscricao/confirmar');
                });
            };
        }
    ]);
})(angular);
