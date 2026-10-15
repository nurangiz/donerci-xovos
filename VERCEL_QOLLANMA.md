# 🚀 Vercel'ga Joylashtirish Qo'llanmasi (Donerci Xovos)

Ushbu loyiha Vercel platformasiga 100% moslashtirilgan bo'lib, ichida maxsus `vercel.json` va `package.json` fayllari mavjud.

---

### 1-USUL: Vercel Dashboard (GitHub orqali) — Eng tavsiya etiladigan usul

1. Ushbu zip faylni oching va fayllarni yangi **GitHub repository** (ombor)ga yuklang (Push qiling).
2. [vercel.com](https://vercel.com) saytiga kiring va o'z hisobingizga kiring (Log in).
3. **"Add New..."** tugmasini bosing va **"Project"** ni tanlang.
4. GitHub'dagi `donerci-xovos` loyihangizni tanlang va **"Import"** tugmasini bosing.
5. Sozlamalarni o'zgartirmasdan **"Deploy"** tugmasini bosing.
6. 10-20 soniyada loyihangiz bepul **`https://donerci-xovos.vercel.app`** domenida butun dunyoga ishga tushadi!

---

### 2-USUL: Vercel CLI (Terminal orqali) — Eng tezkor usul

Agar kompyuteringizda Node.js o'rnatilgan bo'lsa:

1. Terminalda loyiha papkasiga kiring:
   ```bash
   cd donerci-xovos
   ```
2. Quyidagi buyruqni ishga tushiring:
   ```bash
   npx vercel
   ```
3. Terminalda so'ralgan savollarga `Y` (Enter) bosib keting.
4. Production rejimda chiqarish uchun:
   ```bash
   npx vercel --prod
   ```

---

### 3-USUL: Drag & Drop (Netlify Drop orqali - Vercelga muqobil eng oson usul)

Agar sizga hisob ochish yoki GitHub shart bo'lmasa, darhol internetga chiqarish uchun:
1. [app.netlify.com/drop](https://app.netlify.com/drop) saytini oching.
2. `donerci-xovos` papkasini sudrab borib tashlang (Drag & Drop).
3. 5 soniyada tayyor ishlaydigan havola olasiz.
