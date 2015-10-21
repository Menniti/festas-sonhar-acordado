(function(angular){
    var app = angular.module('sonhar.models', [
        'ngResource'
    ]);

    app.factory('pipe', [
        function(){
            return {};
        }
    ]);

    function drf_resource_setup(url) {
        return function($resource){
            var Entity = $resource(url, {'id': '@id'}, {'update': {'method': 'PUT'}});

            Entity.prototype.save = function() {
                // DRF create with POST and update with PUT
                return this.id ? this.$update() : this.$save();
            };

            return Entity;
        };
    }

    app.factory('Subscription', ['$resource', drf_resource_setup('/apiv1/subscriptions/:id')]);
    app.factory('Volunteer', ['$resource', drf_resource_setup('/apiv1/volunteers/:id')]);
    app.factory('Training', ['$resource', drf_resource_setup('/apiv1/trainings/:id')]);

    app.service('cepcoder', ['$q', '$http', function($q, $http){
        this.code = function(cep) {
            var deferred = $q.defer();
            cep = (cep || '').replace(/[^\d]/g, '');

            if(cep.match(/^\d{8,8}$/)){
                return $http.get('http://cep.correiocontrol.com.br/'+cep+'.json');
            }
            deferred.reject('Formato inválido para cep');
            return deferred.promise;
        };
    }]);

})(angular);
