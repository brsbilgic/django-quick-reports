(function() {
    'use strict';

    angular
        .module('jrApp.model.services')
        .factory('Models', Models);

    Models.inject = ['$http'];

    function Models($http) {
        return {
            'all': all
        };

        function all() {
            return $http.get('api/models/');
        }
    }

})();