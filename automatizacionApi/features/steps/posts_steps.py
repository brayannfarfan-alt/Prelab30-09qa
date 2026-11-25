from behave import given, when, then
from services.posts_service import PostsService


@given("que el servicio de Posts esta disponible")
def step_iniciar_servicio( context ):
    context.posts_service = PostsService()


@when('consulto el post con id "{posts_id}"')
def step_consultar_post(context, posts_id):

    context.response = context.posts_service.obtener_post_por_id(posts_id)




@then("el codigo de estado de la respuesta debe ser {status_code:d}")
def step_verificar_status_code(context, status_code):
    actual = context.response.status_code
    assert actual == status_code , f"se esperaba {status_code} pero se obtuvo {actual}"

@then('el campo "{campo}" de la repsuesta debe ser {valor_esperado:d}')
def step_verificar_campo_numerico(context , campo, valor_esperado):
    body = context.response.json()
    assert body.get(campo) == valor_esperado , f"se esperaba {campo}={valor_esperado} pero se obtuvo {body.get(campo)}"


@then('la respuesta debe contener el campo "{campo}"')
def step_verificar_existencia_campo(context , campo):
    body = context.response.json()
    assert campo in body

