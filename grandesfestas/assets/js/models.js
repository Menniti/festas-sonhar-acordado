(function(angular){
    var app = angular.module('sonhar.models', [
        'ngResource'
    ]);

    app.factory('pipe', [
        function(){
            return {};
        }
    ]);

    app.factory('Subscription', ['$resource',
        function($resource){
            return $resource(
                '/apiv1/subscriptions/:id',
                {'id': '@id'},
                {'update': {'method': 'PUT'}}
            );
        }
    ]);

    app.factory('Volunteer', ['$resource',
        function($resource){
            return $resource(
                '/apiv1/volunteers/:id',
                {'id': '@id'},
                {'update': {'method': 'PUT'}}
            );
        }
    ]);

    app.factory('Training', ['$resource',
        function($resource){
            return $resource(
                '/apiv1/trainings/:id',
                {'id': '@id'},
                {'update': {'method': 'PUT'}}
            );
        }
    ]);

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
