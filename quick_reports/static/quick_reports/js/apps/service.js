(function() {
    'use strict';

    angular
        .module('jrApp.app.services')
        .factory('App', App);

    App.inject = ['$http'];

    function App($http) {
        return {
            'all': all
        };

        function all() {
            return $http.get('api/apps/');
        }
    }

})();