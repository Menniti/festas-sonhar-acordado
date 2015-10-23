(function(angular){
    var app = angular.module('sonhar', [
        'ngRoute',
        'sonhar.controllers',
        'sonhar.models'
    ]);

    app.config(function setup($httpProvider, $resourceProvider, $sceDelegateProvider) {
        //setup django
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $resourceProvider.defaults.stripTrailingSlashes = false;

        $sceDelegateProvider.resourceUrlWhitelist([
            /^https?:\/\/(www\.)?youtube\.com\/.*/,
            /^https?:\/\/(www\.)?(sandbox\.)?paypal\.com\/.*/,
            'self',
        ]);
    });

    app.config(function setup_routes($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: 'partials/home.html'
            }).
            when('/inscricao', {
                templateUrl: 'partials/subscription_1_info.html',
                controller: 'SubscriptionInfoCtrl'
            }).
            when('/inscricao/treinamento', {
                templateUrl: 'partials/subscription_2_training.html',
                controller: 'SubscriptionTrainingCtrl'
            }).
            when('/inscricao/pagamento', {
                templateUrl: 'partials/subscription_3_payment.html',
                controller: 'SubscriptionPaymentCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });

    });

    window.addEventListener('load', function(evt){
        angular.bootstrap(document.documentElement, ['sonhar']);
    });
})(angular);