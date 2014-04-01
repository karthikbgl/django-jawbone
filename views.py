import datetime
from jawbone import Jawbone
from django.conf import settings

def get_jawbone():

    client_id = settings.JAWBONE_CLIENT_ID
    client_secret = settings.JAWBONE_APP_SECRET
    redirect_uri = settings.JAWBONE_REDIRECT_URL
    scope = settings.JAWBONE_SCOPE

    jawbone = Jawbone(client_id=client_id,
                      client_secret=client_secret,
                      redirect_uri=redirect_uri,
                      scope=scope)

    return jawbone


def get_jawbone_token(user, jawbone, code):

    token_dict = jawbone.access_token(code)
    expires_at = datetime.datetime.now() + datetime.timedelta(days=365)

    defaults = {
        'access_token': token_dict.get('access_token'),
        'token_type': token_dict.get('token_type'),
        'expires_at': expires_at,
        'refresh_token': token_dict.get('refresh_token')
    }

    jawbone_user, _ = UserJawbone.objects.get_or_create(user=user,
                                 defaults= defaults)

    return jawbone_user


def authorize_jawbone(request):

    jawbone = get_jawbone()
    auth_url = jawbone.auth()

    return redirect(auth_url)


def authorize_jawbone_complete(request):

    error = request.GET.get('error')
    if error:
        message = error

    else:
        jawbone_user = None
        message = "Something went wrong."

        jawbone = get_jawbone()
        code = request.GET.get('code')
        if code:
            jawbone_user = get_jawbone_token(request.user, jawbone, code)
            message = "Jawbone successfully authorized"

    return render_to_response(template, context, context_instance=RequestContext(request))
