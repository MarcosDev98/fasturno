from flask import Blueprint, request, jsonify
from models.Usuario import Usuario
from configs.database import db

usuarios_bp = Blueprint("usuarios", __name__)

# GET todos los usuarios
@usuarios_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
  usuarios = Usuario.query.all()
  data = [
    {"id": u.id, "nombre": u.nombre, "apellido": u.apellido, "email": u.email}
    for u in usuarios
  ]
  return jsonify(data)

# POST crear usuario
@usuarios_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    # Intenta obtener el JSON de la solicitud
    data = request.json
    
    # Valida si la data es None
    if not data:
        return jsonify({"message": "La peticion debe tener un cuerpo JSON valido"}), 400

    
    try:
        u = Usuario()
        u.nombre = data["nombre"]
        u.apellido = data["apellido"],
        u.email = data["email"],
        u.password = data["password"],
        u.is_deleted = "N"
        
        db.session.add(u)
        db.session.commit()
    
        return jsonify({"message": "Usuario creado", "id": u.id}), 201
    
    except KeyError as e:
        return jsonify({"message": f"Faltan datos en el JSON: {e}"}), 400


# GET usuario por id
@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def obtener_usuario(id):
    u = Usuario.query.get_or_404(id)
    return jsonify({"id": u.id, "nombre": u.nombre, "apellido": u.apellido, "email": u.email})

# PUT actualizar usuario
@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    data = request.json

    if not data:
        return jsonify({"message": "La petición debe tener un cuerpo JSON válido"}), 400

    u = Usuario.query.get_or_404(id)
    u.nombre = data.get("nombre", u.nombre)
    u.apellido = data.get("apellido", u.apellido)
    u.email = data.get("email", u.email)
    u.password = data.get("password", u.password)
    db.session.commit()
    return jsonify({"message": "Usuario actualizado"})

# DELETE usuario
@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    u = Usuario.query.get_or_404(id)
    db.session.delete(u)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado"})