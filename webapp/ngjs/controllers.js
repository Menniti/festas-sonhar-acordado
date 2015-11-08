(function(angular){
    var app = angular.module('sonhar.controllers', []);

    app.controller('SubscriptionInfoCtrl', [
        '$scope', '$location', '$timeout', 'Volunteer', 'Subscription', 'pipe', 'cepcoder',
        function($scope, $location, $timeout, Volunteer, Subscription, pipe, cepcoder){

            function debounce_watch(callback, timeout) {
                var timeout_id = null;
                return function(before, now) {
                    if(before !== now && now !== '') { 
                        if(timeout_id) {
                            $timeout.cancel(timeout_id);
                        }
                        timeout_id = $timeout(function(){
                            callback(before, now);
                        }, timeout);
                    }
                };
            }

            $scope.volunteer = pipe.volunteer || new Volunteer();

            /**
             * Find existing profile id
             */
            function recover_id(){
                var query = {'email': $scope.volunteer.email};
                Volunteer.query(query, function(results){
                    $scope.volunteer.id = results.length === 1 ? results[0].id : undefined;
                });
            }

            $scope.$watch('volunteer.email', debounce_watch(recover_id, 500));

 
            /** 
             * Find address
             */
            function populate_address_from_cep() {
                cepcoder.code($scope.volunteer.cep).then(function(resp) {
                    var data = resp.data;
                    $scope.volunteer.address = data.logradouro || '';
                    $scope.volunteer.city = data.localidade || '';
                    $scope.volunteer.state = data.uf || '';
                });
            }

            $scope.$watch('volunteer.cep', debounce_watch(populate_address_from_cep, 500));

            $scope.save = function() {
                $scope.volunteer.save().then(function(){
                    pipe.volunteer = $scope.volunteer;
                    $location.path('/inscricao/treinamento');
                });
            };
        }
    ]);

    app.controller('SubscriptionTrainingCtrl', ['$scope', '$location', 'Training', 'Subscription', 'pipe',
        function($scope, $location, Training, Subscription, pipe) {
            $scope.volunteer = pipe.volunteer;
            $scope.subscription = new Subscription();

            $scope.subscription.volunteer = $scope.volunteer.id;

            Subscription.query({'volunteer': $scope.volunteer.id}, function(res) {
                console.log(res);
                if(res.length > 0) {
                    $scope.subscription = res[0];
                }
            });

            Training.query(function(list){
                training_list = list;
                $scope.training_list = training_list;
            });

            $scope.save = function() {
                $scope.subscription.save().then(function(){
                    pipe.subscription = $scope.subscription;
                    $location.path('/inscricao/pagamento');
                });
            };
        }
    ]);

    app.controller('SubscriptionPaymentCtrl', ['$scope', '$location', 'PaymentFormData', 'pipe',
        function($scope, $location, PaymentFormData, pipe) {
            window.PaymentFormData = PaymentFormData;
            $scope.subscription = pipe.subscription;
            console.log($scope.subscription);

            $scope.form_data = PaymentFormData.get({
                'subscription_id': $scope.subscription.id
            });

            $scope.save = function() {
                var promise = $scope.subscription.id ? $scope.subscription.$update() : $scope.subscription.$save();

                promise.then(function(){
                    $location.path('/inscricao/pagamento');
                });
            };
        }
    ]);

})(angular);
