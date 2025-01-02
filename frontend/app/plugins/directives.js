export default defineNuxtPlugin(nuxtApp => {
  nuxtApp.vueApp.directive('click-outside', {
    beforeMount(el, binding) {
      // Check if the modal is visible
      el.clickOutsideEvent = function (event) {
        if (el.contains(event.target)) return; // Clicked inside the modal

        if (binding.value && typeof binding.value === 'function') {
          // Call the method provided in the directive
          binding.value(event);
        }
      };
      document.body.addEventListener('click', el.clickOutsideEvent);
    },
    unmounted(el) {
      document.body.removeEventListener('click', el.clickOutsideEvent);
    },
  });
});