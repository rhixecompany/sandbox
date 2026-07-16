# RESEARCH_REPORT — xamehi.tv

> **Type:** Project research report | **Updated:** 2026-07-10

**Type:** Django REST + React streaming platform
**Tech Stack:** Django DRF, React 17, MUI 4, Redux, SimpleJWT, django-allauth, PostgreSQL, PayPal
**Status:** Active

---

## Similar Projects

| Project | URL | Why Relevant |
| --------- | ----- | -------------- |
| DRF + SimpleJWT auth | <https://www.django-rest-framework.org/api-guide/authentication/> | DRF JWT authentication |
| MUI v4 → v5 migration | <https://mui.com/material-ui/migration/migration-v4/> | Material-UI v4 to v5 migration |
| ra-data-django-rest-framework | <https://github.com/bmihelac/ra-data-django-rest-framework> | React Admin DRF data provider |
| video-react | <https://github.com/video-react/video-react> | Video player for React |
| react-paypal-button-v2 | <https://github.com/Luehang/react-paypal-button-v2> | PayPal React integration |

---

## Key Findings

### DRF + React 17 Streaming Platform Patterns (2026)

**Core Architecture:**

- Django REST Framework + React 17 (CRA-based) remains a solid stack for 2026 streaming platforms
- Django 5.2 LTS + DRF 3.16 provide full stability and long-term support
- PostgreSQL recommended for production (JSONB support for video metadata, better concurrency)
- Gunicorn + WhiteNoise for small-to-medium deployments; add nginx/CDN for video delivery at scale

**Streaming-Specific Patterns:**

- **Video metadata API**: Use DRF ViewSets with custom actions for HLS/DASH manifest generation
- **Media serving**: Serve static files via WhiteNoise/CDN; stream video via signed URLs or token auth
- **Range requests**: Django's `FileResponse` supports HTTP 206 Partial Content for video seeking
- **Transcoding pipeline**: FFmpeg + Celery async tasks for HLS/DASH generation on upload
- **DRF serialization**: Nested serializers for Video → Renditions/Qualities → Segments hierarchy

**Relevant Resource:**

- Django REST Framework tutorial 2026: <https://tech-insider.org/django-rest-framework-tutorial-python-api-2026>
- Reddit discussion on React+DRF stack viability 2026: <https://www.reddit.com/r/django/comments/1r4nkut/is_react_djangodrf_still_a_solid_stack_in_ai_era>

---

### React 17 + Material-UI 4 → React 18 + MUI 5 Migration

**MUI v4 → v5 Key Changes (from official migration guide):**

- **Styling engine**: JSS → Emotion (biggest breaking change)
- **Package rename**: `@material-ui/*` → `@mui/*`
- **React minimum**: v17.0.0 (React 18 fully supported)
- **TypeScript minimum**: v3.5
- **Default variants**: TextField `outlined`, Link `underline="always"`

**Migration Tools (Automated):**

```bash
# Core codemod - handles ~80% of changes
npx @mui/codemod v5.0.0/preset-safe

# Variant props (TextField, Button, etc.)
npx @mui/codemod v5.0.0/variant-prop

# Link underline behavior
npx @mui/codemod v5.0.0/link-underline-hover
```

**Manual Changes Required:**

- Replace `makeStyles`/`withStyles` with `styled()` or `sx` prop
- Migrate `createMuiTheme` → `createTheme`; `ThemeProvider` import from `@mui/material/styles`
- Update all imports: `@material-ui/core` → `@mui/material`, `@material-ui/icons` → `@mui/icons-material`
- Add Emotion peer dependencies: `npm install @emotion/react @emotion/styled`

**React 17 → 18 Upgrade:**

- Update `index.js`: `ReactDOM.render()` → `ReactDOM.createRoot().render()`
- Automatic batching, concurrent features opt-in
- Mostly backward compatible; test `act()` warnings in tests
- React 18 docs: <https://react.dev/blog/2022/03/08/react-18-upgrade-guide>

**Full MUI Migration Guide:** <https://mui.com/material-ui/migration/migration-v4/>

---

### video-react Player Integration with DRF Backend

**video-react capabilities:**

- Native HLS (via hls.js) and DASH (via dash.js) support
- Props: `src` (string or array of sources), `poster`, `autoPlay`, `controls`, `playsInline`
- Event handlers: `onPlay`, `onPause`, `onEnded`, `onError`, `onProgress`
- Custom controls via `Player` sub-components

**Integration Pattern with DRF:**

```jsx
// Frontend: VideoPlayer.jsx
import { Player } from 'video-react';

<Player
  playsInline
  src={[
    { src: video.hls_manifest_url, type: 'application/x-mpegURL' },
    { src: video.dash_manifest_url, type: 'application/dash+xml' },
    { src: video.mp4_url, type: 'video/mp4' } // fallback
  ]}
  poster={video.thumbnail_url}
  onError={(e) => handleError(e)}
/>
```

```python
# Backend: serializers.py
class VideoSerializer(serializers.ModelSerializer):
    hls_manifest_url = serializers.SerializerMethodField()
    dash_manifest_url = serializers.SerializerMethodField()
    
    def get_hls_manifest_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/api/videos/{obj.id}/manifest.m3u8')
```

**HLS/DASH Generation (Django + Celery + FFmpeg):**

- Upload → trigger Celery task → FFmpeg transcode to multiple renditions
- Generate `.m3u8` (HLS) and `.mpd` (DASH) manifests
- Store in media storage (S3/GCS for production) or local media root
- Serve manifests via DRF views with token authentication

**Alternative Players:**

- **react-player**: <https://github.com/cookpete/react-player> - supports HLS, DASH, YouTube, Vimeo
- **react-all-player**: <https://dev.to/asadk/reactallplayer-one-player-to-rule-them-all-mp4-hls-dash-youtube-vimeo-1hoc> - unified API for all formats
- **dash.js directly**: <https://www.smashingmagazine.com/2025/03/adaptive-video-streaming-dashjs-react> - full ABR control

---

### PayPal Integration with Django REST + React Frontend

**Frontend (react-paypal-button-v2):**

```jsx
import PayPalButton from 'react-paypal-button-v2';

<PayPalButton
  amount={video.price}
  currency="USD"
  onSuccess={(details, data) => {
    // Call DRF endpoint to verify payment
    fetch('/api/payments/verify/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${accessToken}` },
      body: JSON.stringify({ orderID: data.orderID })
    });
  }}
  options={{
    clientId: process.env.REACT_APP_PAYPAL_CLIENT_ID,
    // For subscriptions: vault=true, intent='subscription'
  }}
/>
```

**Backend (DRF):**

```python
# views.py
class PayPalVerifyPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        order_id = request.data.get('orderID')
        # Verify with PayPal API
        access_token = get_paypal_access_token()
        response = requests.get(
            f'https://api.paypal.com/v2/checkout/orders/{order_id}',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        if response.json()['status'] == 'COMPLETED':
            # Grant video access
            VideoAccess.objects.create(user=request.user, video_id=video_id)
            return Response({'status': 'success'})
        return Response({'status': 'failed'}, status=400)
```

**Webhook Verification (Critical for Production):**

- Register webhook endpoint in PayPal Developer Dashboard
- Verify `PAYMENT.CAPTURE.COMPLETED` events
- Validate webhook signature using `PAYPAL_WEBHOOK_ID` and `verify_webhook_signature`

**Resources:**

- react-paypal-button-v2: <https://github.com/Luehang/react-paypal-button-v2>
- Django + React PayPal tutorial: <https://justdjango.com/blog/django-react-paypal-payments>

---

### SimpleJWT + django-allauth Social Authentication Patterns

**Integration Pattern (2026 Best Practice):**

```python
# settings.py
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# SimpleJWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# allauth settings
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
SOCIALACCOUNT_ADAPTER = 'myapp.adapters.SocialAccountAdapter'

# URL routing - namespace to avoid conflicts
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('allauth.urls')),  # /accounts/google/login/, etc.
]
```

**Custom Social Adapter for JWT:**

```python
# adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from rest_framework_simplejwt.tokens import RefreshToken

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        # Generate JWT tokens on social login
        refresh = RefreshToken.for_user(user)
        request.session['jwt_access'] = str(refresh.access_token)
        request.session['jwt_refresh'] = str(refresh)
        return user
```

**Frontend Flow:**

1. User clicks "Login with Google" → redirects to `/accounts/google/login/`
2. allauth handles OAuth flow → creates/links User
3. Custom adapter generates JWT → returns to frontend callback URL
4. Frontend extracts tokens from URL params or session → stores in memory (not localStorage)

**Key Pitfall:** URL namespace conflicts between SimpleJWT (`/api/token/`) and allauth (`/accounts/`). Always namespace allauth URLs.

---

### Redux Toolkit Migration from Redux 4 + redux-thunk

**Current Legacy Pattern (xamehi.tv):**

```javascript
// store.js - legacy
import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';
import videoReducer from './reducers/videoReducer';
import authReducer from './reducers/authReducer';

const rootReducer = combineReducers({ video: videoReducer, auth: authReducer });
const store = createStore(rootReducer, applyMiddleware(thunk));
```

**Modern Redux Toolkit Pattern:**

```javascript
// store.js - modern
import { configureStore } from '@reduxjs/toolkit';
import videoSlice from './slices/videoSlice';
import authSlice from './slices/authSlice';

export const store = configureStore({
  reducer: {
    video: videoReducer,
    auth: authReducer,
  },
  // RTK includes thunk by default; customize if needed
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST', 'persist/REHYDRATE'],
      },
    }),
});
```

**Slice Migration (reducer + actions + thunks → single file):**

```javascript
// slices/videoSlice.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchVideos = createAsyncThunk('video/fetchVideos', async () => {
  const response = await axios.get('/api/videos/');
  return response.data;
});

const videoSlice = createSlice({
  name: 'video',
  initialState: { items: [], status: 'idle', error: null },
  reducers: {
    clearError: (state) => { state.error = null; },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchVideos.pending, (state) => { state.status = 'loading'; })
      .addCase(fetchVideos.fulfilled, (state, action) => {
        state.items = action.payload;
        state.status = 'succeeded';
      })
      .addCase(fetchVideos.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      });
  },
});

export const { clearError } = videoSlice.actions;
export default videoSlice.reducer;
```

**RTK Query (Replace redux-thunk for API calls):**

```javascript
// api/videoApi.js
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const videoApi = createApi({
  reducerPath: 'videoApi',
  baseQuery: fetchBaseQuery({ 
    baseUrl: '/api/',
    prepareHeaders: (headers, { getState }) => {
      const token = getState().auth.accessToken;
      if (token) headers.set('Authorization', `Bearer ${token}`);
      return headers;
    },
  }),
  tagTypes: ['Video'],
  endpoints: (builder) => ({
    getVideos: builder.query({
      query: () => 'videos/',
      providesTags: ['Video'],
    }),
    getVideo: builder.query({
      query: (id) => `videos/${id}/`,
      providesTags: (result, error, id) => [{ type: 'Video', id }],
    }),
    createVideo: builder.mutation({
      query: (video) => ({ url: 'videos/', method: 'POST', body: video }),
      invalidatesTags: ['Video'],
    }),
  }),
});

export const { useGetVideosQuery, useGetVideoQuery, useCreateVideoMutation } = videoApi;
```

**Migration Guide:** <https://redux-toolkit.js.org/usage/migrating-to-modern-redux>
**RTK Query Migration:** <https://redux-toolkit.js.org/rtk-query/usage/migrating-to-rtk-query>

---

### React Admin Dashboard with DRF Backend Customization

**Data Provider (ra-data-django-rest-framework):**

```javascript
// App.js
import { Admin, Resource } from 'react-admin';
import drfProvider, { jwtTokenAuthProvider, fetchJsonWithAuthJWTToken } from 'ra-data-django-rest-framework';
import { VideoList, VideoCreate, VideoEdit } from './components/admin';

const authProvider = jwtTokenAuthProvider();
const dataProvider = drfProvider('/api', fetchJsonWithAuthJWTToken);

<Admin authProvider={authProvider} dataProvider={dataProvider}>
  <Resource name="videos" list={VideoList} create={VideoCreate} edit={VideoEdit} />
  <Resource name="users" list={UserList} />
</Admin>
```

**Key Features of ra-data-django-rest-framework:**

- **Pagination**: Works with DRF `PageNumberPagination` (set `page_size_query_param = 'page_size'`)
- **Sorting**: Supports DRF `OrderingFilter`
- **Filtering**: Maps React Admin filters to DRF filter backends
- **Authentication**: `jwtTokenAuthProvider` for SimpleJWT (`/api/token/` endpoint)
- **Example app included** with Django backend + React Admin frontend

**Customization Patterns:**

```javascript
// Custom data provider for video-specific endpoints
import { fetchUtils } from 'react-admin';

const videoDataProvider = {
  ...drfProvider('/api', fetchJsonWithAuthJWTToken),
  
  // Custom method for video streaming manifests
  getVideoManifest: (videoId) => ({
    url: `/api/videos/${videoId}/manifest.m3u8`,
    options: { headers: { 'Accept': 'application/vnd.apple.mpegurl' } }
  }),
};
```

**Resource:** <https://github.com/bmihelac/ra-data-django-rest-framework>

---

### WhiteNoise Static Files Serving Django Production

**Configuration (settings.py):**

```python
# Middleware - WhiteNoise after SecurityMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- Add here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise storage - compressed + manifest (cache busting)
STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# Optional: Brotli compression (requires `pip install whitenoise[brotli]`)
# WHITENOISE_BROTLI = True

# Production: Use CDN
import os
STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
STATIC_URL = f'{STATIC_HOST}/static/' if STATIC_HOST else '/static/'
```

**Key Features:**

- Auto-generates versioned filenames with MD5 hashes (cache busting)
- Gzip + Brotli compression
- Serves `index.html` for SPA fallback (`WHITENOISE_INDEX_FILE = True`)
- `collectstatic` still required; WhiteNoise serves from `STATIC_ROOT`

**For Video Files (Media):**

- WhiteNoise only serves **static** files, not user uploads
- Use `django-storages` + S3/GCS for video media in production
- Or nginx/X-Accel-Redirect for protected media

**Documentation:** <https://whitenoise.readthedocs.io/en/stable/django.html>

---

### CRA → Vite/Next.js Migration for Streaming Frontend

**Why Migrate from CRA:**

- CRA deprecated (React team no longer recommends it)
- Slow builds, no native ESM, limited customization
- Vite: instant HMR, optimized builds, native ES modules
- Next.js: SSR/SSG, App Router, server components, better SEO

**Migration Paths:**

| Target | Best For | Effort |
| -------- | ---------- | -------- |
| **Vite** | SPA streaming app (no SSR needed) | Low (~1 day) |
| **Next.js App Router** | SEO, auth, server components | Medium (~1 week) |
| **Next.js Pages Router** | Incremental migration | Medium |

**CRA → Vite Steps:**

```bash
# 1. Install Vite
npm create vite@latest frontend -- --template react

# 2. Copy src/ files, update imports
# 3. Replace react-scripts with vite in package.json scripts
# 4. Update index.html (Vite uses root index.html)
# 5. Handle environment variables: REACT_APP_ → VITE_
# 6. Proxy config: vite.config.js server.proxy
# 7. Test build: npm run build
```

**Vite Config for Django Backend:**

```javascript
// vite.config.js
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': 'http://127.0.0.1:8000',
      '/media': 'http://127.0.0.1:8000',
    },
  },
  build: {
    outDir: '../django_project/staticfiles/frontend',  // or separate deploy
  },
});
```

**Next.js Migration Guide:** <https://nextjs.org/docs/app/guides/migrating/from-create-react-app>
**Vite Migration Guide:** <https://adhithiravi.medium.com/migrating-from-create-react-app-to-vite-a-modern-approach-76148adb8983>

---

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
| ------- | ---------- | ------ |
| MUI v4→v5 migration | <https://mui.com/material-ui/migration/migration-v4/> | Migration Guide |
| React 18 upgrade | <https://react.dev/blog/2022/03/08/react-18-upgrade-guide> | Guide |
| DRF SimpleJWT | <https://django-rest-framework-simplejwt.readthedocs.io/> | Docs |
| django-allauth | <https://docs.allauth.org/> | Docs |
| PayPal Developer | <https://developer.paypal.com/> | API Docs |
| ra-data-drf | <https://github.com/bmihelac/ra-data-django-rest-framework> | Data Provider |
| Redux Toolkit | <https://redux-toolkit.js.org/> | Docs |
| RTK Query | <https://redux-toolkit.js.org/rtk-query/overview> | Docs |
| WhiteNoise | <https://whitenoise.readthedocs.io/en/stable/django.html> | Docs |
| video-react | <https://github.com/video-react/video-react> | Player Lib |
| react-paypal-button-v2 | <https://github.com/Luehang/react-paypal-button-v2> | PayPal React |
| CRA → Next.js | <https://nextjs.org/docs/app/guides/migrating/from-create-react-app> | Migration |
| CRA → Vite | <https://vitejs.dev/guide/#migrating-from-create-react-app> | Migration |

---

## Best Practices

1. **Upgrade React 17→18** — auto-batching, Concurrent Features; mostly backward compatible
2. **Migrate MUI v4→v5** — use codemods; Emotion replaces JSS
3. **RTK Query** — replace redux-thunk for API data fetching and caching
4. **JWT security** — short-lived access tokens (5–15 min), refresh rotation; memory storage only
5. **CORS restriction** — django-cors-headers with explicit allowed origins
6. **Video streaming** — use signed URLs or token-authenticated manifests; serve via CDN
7. **PayPal webhooks** — validate signatures before processing payments
8. **React Admin DRF** — use `ra-data-django-rest-framework` for zero-config integration
9. **Static files** — WhiteNoise for static; S3/GCS + django-storages for video media
10. **Frontend build** — migrate CRA → Vite (SPA) or Next.js (SSR/SEO)

---

## Common Pitfalls

| Pitfall | Impact | Avoidance |
| --------- | -------- | ----------- |
| MUI v4 JSS → Emotion | Styling breaks | Use codemods (`@mui/codemod`) |
| React createRoot missing | App won't render | Update to `createRoot()` in index.js |
| SimpleJWT + allauth URL conflicts | Auth routes clash | Namespace allauth URLs under `/accounts/` |
| CORS + proxy confusion | Frontend can't reach backend | Test production config early; separate dev/prod CORS |
| Redux-thunk boilerplate | Verbose, error-prone | Migrate to RTK Query + createSlice |
| WhiteNoise serving media | Videos don't load in prod | Use django-storages + S3 for media files |
| PayPal client-side only | Payment spoofing risk | Always verify on backend via webhook/API |
| Video manifest CORS | Player can't load HLS/DASH | Add CORS headers to manifest/media responses |
| Legacy Redux + React 18 | Potential compatibility issues | Migrate to Redux Toolkit |

---

## Performance

1. **React 18 auto-batching** — fewer re-renders in async contexts
2. **RTK Query caching** — built-in invalidation and deduplication
3. **MUI v5 Emotion** — smaller runtime than JSS
4. **Gunicorn + WhiteNoise** — sufficient for moderate traffic; CDN for video
5. **Video delivery** — HLS/DASH adaptive bitrate; CDN with edge caching
6. **Database** — PostgreSQL with indexes on video lookup fields; consider read replicas
7. **API pagination** — DRF `PageNumberPagination` with configurable page size

---

## Security

1. **SimpleJWT token blacklist** — enable to revoke compromised refresh tokens
2. **PayPal webhook verification** — validate signatures before processing
3. **django-allauth** — restrict allowed social providers; whitelist callback URLs
4. **CORS restriction** — limit to frontend domain only
5. **Video access control** — signed URLs with expiry; token-authenticated manifests
6. **HTTPS everywhere** — enforce in production (SECURE_SSL_REDIRECT, HSTS)
7. **Content Security Policy** — restrict script/style sources; nonce for inline scripts
8. **Rate limiting** — DRF throttling on auth/payment endpoints

---

## Related Projects (in workspace)

- **ecom** — shares DRF + PayPal + React; uses React 18/Redux Toolkit (more modern)
- **profile** — Django monolith; xamehi.tv adds React frontend
- **rhixecompany-comics** — dual-stack platform; xamehi.tv is simpler (single Django)
- **selenium_webdriver** — browser automation with Selenium
- **xamehi** — same Django + React pattern; xamehi adds Express backend

---

## Resources

| Resource | URL | Description |
| ---------- | ----- | ------------- |
| React 18 Docs | <https://react.dev/> | React official documentation |
| MUI v5 | <https://mui.com/> | Material-UI v5 documentation |
| SimpleJWT | <https://django-rest-framework-simplejwt.readthedocs.io/> | DRF JWT auth docs |
| django-allauth | <https://docs.allauth.org/> | Social auth integration |
| PayPal Developer | <https://developer.paypal.com/> | PayPal API documentation |
| ra-data-drf | <https://github.com/bmihelac/ra-data-django-rest-framework> | React Admin DRF provider |
| video-react | <https://github.com/video-react/video-react> | Video player component |
| react-paypal-button-v2 | <https://github.com/Luehang/react-paypal-button-v2> | PayPal React buttons |
| Redux Toolkit | <https://redux-toolkit.js.org/> | Modern Redux |
| WhiteNoise | <https://whitenoise.readthedocs.io/> | Static files serving |
| Django 5.2 LTS | <https://www.djangoproject.com/download/5.2/roadmap/> | Django LTS roadmap |
| DRF 3.16 | <https://www.django-rest-framework.org/> | DRF documentation |

---

## Research Notes (Section 13 Queries - Addressed)

| Query | Status | Key Findings |
| ------- | -------- | -------------- |
| Django REST Framework + React 17 streaming platform patterns 2026 | ✅ | DRF 3.16 + Django 5.2 LTS; PostgreSQL; Gunicorn+WhiteNoise; signed URLs for video |
| React 17 + Material-UI 4 migration to React 18 + MUI 5 | ✅ | Codemods automate 80%; JSS→Emotion; package rename @material-ui→@mui |
| video-react player integration with DRF backend | ✅ | HLS/DASH via src array; FFmpeg+Celery for transcoding; token auth on manifests |
| PayPal integration with Django REST + React frontend | ✅ | react-paypal-button-v2 frontend; DRF verify endpoint + webhook validation |
| SimpleJWT + django-allauth social authentication patterns | ✅ | Namespace URLs; custom adapter generates JWT on social login |
| Redux Toolkit migration from legacy Redux + redux-thunk | ✅ | configureStore + createSlice + createAsyncThunk; RTK Query replaces thunks |
| React Admin dashboard with DRF backend customization | ✅ | ra-data-django-rest-framework provides JWT auth, pagination, filtering |
| WhiteNoise static files serving Django production | ✅ | CompressedManifestStaticFilesStorage; CDN for production; media→S3 |

---

## Implementation Priority Recommendations

### Phase 1: Critical Upgrades (Week 1-2)

1. **React 17 → 18 + MUI 4 → 5** — Use codemods; test thoroughly
2. **Redux → Redux Toolkit + RTK Query** — Reduces boilerplate ~60%
3. **CRA → Vite** — Immediate DX improvement; ~1 day migration

### Phase 2: Video Pipeline (Week 3-4)

1. **HLS/DASH transcoding** — FFmpeg + Celery; generate manifests on upload
2. **Token-authenticated manifests** — Secure video delivery
3. **CDN integration** — CloudFront/Cloudflare for video segments

### Phase 3: Auth & Payments (Week 5)

1. **SimpleJWT + allauth integration** — Social login with JWT tokens
2. **PayPal webhook verification** — Production-ready payment flow

### Phase 4: Admin & Polish (Week 6)

1. **React Admin customization** — Video-specific fields, manifest preview
2. **WhiteNoise + S3 media** — Production static/media configuration
