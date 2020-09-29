new Vue({
    el: '#main_app',
    data: {
        districts: []
    },
    created: function (){
        const vm = this;
        axios.get('/api/districts')
            .then(function (response){
                vm.districts = response.data
            })
    }
})