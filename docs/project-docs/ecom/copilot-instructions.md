# Copilot Instructions — ecom

## Python/Django
- Django conventions, PEP 8
- DRF ViewSets + Serializers for API
- JWT authentication via SimpleJWT

## JavaScript/React
- ESLint with react-app presets
- Redux pattern: constants → actions → reducers → components
- React Bootstrap for UI components
- Axios for API calls with JWT tokens

## File Organization
- Components in `frontend/src/components/`
- Screens in `frontend/src/screens/`
- Redux logic in `actions/`, `reducers/`, `constants/`

## Security
- Never commit SECRET_KEY
- JWT tokens for API auth
- CORS configured via django-cors-headers
- Validate inputs via DRF serializers
