(function() {
//<!--declare modules which depends from ngROute from angular
//configuring navigation routes of page -->

    var app = angular.module('AppChat',['ngStorage','ngRoute']);
    

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location,loggedUser) {
        $routeProvider.when('/login', { //first route
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
            }).when('/home', {
            templateUrl: 'pages/home.html',
            controller: 'HomeController',
            controllerAs : 'homeCtrl'//controlers
             }).when('/:gid/contacts', {
            templateUrl: 'pages/groupUsers.html',
            controller: 'ContactController',
            controllerAs : 'contactCtrl'//controlers
             }).when('/groups', { //detail from specific part, i can add /chat/gid or smthng
            templateUrl: 'pages/chatgroups.html',
            controller: 'GroupChatController',
            controllerAs : 'groupChatCtrl' //controlers
             }).when('/groups/:gid/messages', {
            templateUrl: 'pages/messages.html',
            controller: 'MessageController',
            controllerAs : 'msgCtrl' //controlers
            }).when('/groups/:gid/hashtags', {
            templateUrl: 'pages/hashtags.html',
            controller: 'HashtagController',
            controllerAs : 'hashCtrl'
            }).when('/messages/:mid', {
            templateUrl: 'pages/messagedetail.html',
            controller: 'MessageDetailsController',
            controllerAs : 'msgdtlCtrl' //controlers
             }).when('/register', {
            templateUrl: 'pages/register.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
             }).when('/contacts', {
            templateUrl: 'pages/contacts.html',
            controller: 'ContactController',
            controllerAs : 'contactCtrl'





       /*
        }).when('/chat', { //detail from specific part, i can add /chat/gid or smthng
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl' //controlers
            */

        }).otherwise({ //default routes
            redirectTo: '/login'
        });
    }]);

     app.service('loggedUser', function () {

            this.setUser = function(user) {
                localStorage.setItem('loggedUser',JSON.stringify(user));
                return;
            }
            this.getUser = function() {
                return JSON.parse(localStorage.getItem('loggedUser'));
            }
            this.deleteUser = function() {
                localStorage.removeItem('loggedUser');
            }
});


})();
