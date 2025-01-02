export function useModal() {

    function toggle(isOpen){
        isOpen.value = !isOpen.value;
    }

    function open(isOpen){
        isOpen.value = true;
    }

    function close(isOpen){
        isOpen.value = false;
    }

    return {toggle, open, close}
}