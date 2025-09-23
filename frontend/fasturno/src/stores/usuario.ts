import type { Usuario } from "@/types/usuario";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useUsuarioStore = defineStore("usuario", () => {
  const usuarios = ref<Usuario[]>([]);
  const API_URL = "http://127.0.0.1:5000/usuarios";

  const getUsers = async () => {
    try {
      const response = await fetch(API_URL);
      if (!response.ok) throw new Error("Error al obtener usuarios");
      usuarios.value = await response.json();
    } catch (error) {
      console.error(error);
    }
  };

  const createUser = async (nuevoUsuario: Usuario) => {
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(nuevoUsuario),
      });
      if (!response.ok) throw new Error("Error al crear usuario");
      const data = await response.json();
      usuarios.value.push(data);
    } catch (error) {
      console.error(error);
    }
  };

  const updateUser = async (usuarioModificado: Usuario) => {
    try {
      const response = await fetch(`${API_URL}/${usuarioModificado.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(usuarioModificado),
      });
      if (!response.ok) throw new Error("Error al actualizar usuario");
      const data = await response.json();
      const idx = usuarios.value.findIndex((u) => u.id === usuarioModificado.id);
      if (idx !== -1) usuarios.value[idx] = data;
    } catch (error) {
      console.error(error);
    }
  };

  const deleteUser = async (id: number) => {
    try {
      const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
      if (!response.ok) throw new Error("Error al eliminar usuario");
      usuarios.value = usuarios.value.filter((u) => u.id !== id);
    } catch (error) {
      console.error(error);
    }
  };

  return { usuarios, getUsers, createUser, updateUser, deleteUser };
});
