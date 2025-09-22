import { defineStore } from "pinia";
import { ref } from "vue";

export const useUsuarioStore = defineStore("usuario", () => {
  const usuario = ref();

  const API_URL = "";

  const getUser = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();
    usuario.value = data;
  }

  return {
    usuario,
    getUser
  }

});