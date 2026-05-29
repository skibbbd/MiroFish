# MiroFish - Quick Start Guide

## 🚀 Get Running in 30 Seconds

### Step 1: Start the Application
```bash
npm run dev
```

That's it! Both backend and frontend will start automatically.

- **Backend**: Running on http://localhost:5001
- **Frontend**: Running on http://localhost:5173

### Step 2: Test the API (Optional)
In another terminal:
```bash
python test_api.py
```

This will run through all the main API endpoints and verify everything is working with mock data.

---

## 📋 What's Ready to Test

### No API Keys Needed ✨
The app is configured in **TEST_MODE**, meaning:
- ✅ All APIs return realistic mock data
- ✅ No LLM API keys required
- ✅ No Zep API keys required
- ✅ Full feature testing

### What You Can Test
- **Graph Entities**: Retrieve mock entities by graph ID
- **Entity Filtering**: Filter entities by type (Student, Organization, etc.)
- **Entity Details**: Get detailed information about specific entities
- **Profile Generation**: Mock Reddit/Twitter profiles
- **Simulations**: Create and configure mock simulations
- **Relationships**: Entity relationships and graph structure

---

## 🔧 Manual Testing

### Test Graph Entities
```bash
curl http://localhost:5001/api/simulation/entities/test_graph
```

### Test Entity Filtering
```bash
curl "http://localhost:5001/api/simulation/entities/test_graph?entity_types=Student"
```

### Test by Entity Type
```bash
curl http://localhost:5001/api/simulation/entities/test_graph/by-type/PublicFigure
```

---

## ⚙️ Configuration

Current setup (`.env`):
```env
TEST_MODE=true
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```

### To Use Real APIs Later:
1. Add your API keys to `.env`:
   ```env
   LLM_API_KEY=your_key_here
   ZEP_API_KEY=your_key_here
   ```

2. Set TEST_MODE to false:
   ```env
   TEST_MODE=false
   ```

3. Restart: `npm run dev`

---

## 📂 Project Structure

```
MiroFish/
├── backend/                    # Python Flask backend
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   ├── services/
│   │   │   └── test_data_generator.py  # NEW: Mock data generation
│   │   ├── config.py          # MODIFIED: Added TEST_MODE
│   │   └── models/
│   ├── run.py                 # Start backend
│   └── requirements.txt
├── frontend/                   # Vue.js frontend
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── .env                        # NEW: Test configuration
├── test_api.py                 # NEW: API test script
├── TESTING_GUIDE.md            # NEW: Detailed testing docs
├── TEST_MODE_SETUP.md          # NEW: Implementation details
└── QUICK_START.md              # This file
```

---

## 🧪 What's in Test Mode

### Mock Entity Types
- **Student**: Realistic student names and profiles
- **PublicFigure**: Well-known public figure names
- **Organization**: Company names and profiles
- **Location**: Geographic locations
- **Topic**: Discussion topics and themes

### Mock Data Includes
- Entity IDs, names, types, descriptions
- Properties: age, location, interests
- Relationships: knows, works_with, collaborates
- Profile data for Reddit and Twitter
- Simulation configurations
- Task status tracking

### Realistic Values
- **Names**: Alice Johnson, Elon Musk, TechCorp Inc, etc.
- **Ages**: 25-75 years old
- **Locations**: New York, London, Tokyo, Beijing, etc.
- **Interests**: Technology, Music, Sports, Art, Science
- **Engagement**: High, Medium, Low

---

## 🔍 Verify Everything Works

### Check Backend
```bash
curl http://localhost:5001/api/simulation/entities/demo
```

Should return:
```json
{
  "success": true,
  "data": {
    "graph_id": "demo",
    "filtered_count": 10,
    "entity_types": ["Student", "PublicFigure", "Organization"],
    "entities": [...]
  }
}
```

### Check Frontend
Open http://localhost:5173 in your browser and look for the UI.

### Run Test Suite
```bash
python test_api.py
```

Should show:
```
✅ Passed: 6
❌ Failed: 0
Success Rate: 100.0%
```

---

## 🐛 Troubleshooting

### Backend won't start?
```bash
cd backend
python run.py
# Check for Python 3.11+ and flask installed
```

### Frontend won't start?
```bash
cd frontend
npm install
npm run dev
```

### Can't connect to API?
- Check backend is running: `python backend/run.py`
- Check port 5001 is available
- Check for firewall/network issues

### Want more logging?
```bash
FLASK_DEBUG=true npm run backend
```

---

## 📚 Learn More

- **TESTING_GUIDE.md** - Comprehensive testing documentation
- **TEST_MODE_SETUP.md** - Technical implementation details
- **backend/app/services/test_data_generator.py** - How mock data is generated
- **backend/app/config.py** - Configuration system

---

## ✅ Checklist

- [ ] Backend running on port 5001
- [ ] Frontend running on port 5173
- [ ] TEST_MODE=true in `.env`
- [ ] Can access http://localhost:5173
- [ ] API returns mock data
- [ ] `test_api.py` runs successfully

---

## 🎯 Next Steps

1. **Test the API** using `python test_api.py`
2. **Explore the frontend** at http://localhost:5173
3. **Review mock data** by checking API responses
4. **Add real API keys** when ready (update `.env` and set TEST_MODE=false)
5. **Read documentation** in TESTING_GUIDE.md for advanced features

---

## 📞 Quick Commands

```bash
# Start everything
npm run dev

# Backend only
cd backend && python run.py

# Frontend only
cd frontend && npm run dev

# Test APIs
python test_api.py

# With more debug output
FLASK_DEBUG=true npm run dev

# Install dependencies
npm run setup
npm run setup:backend
npm run setup:all
```

---

**You're all set!** 🎉

The application is ready to test with realistic mock data and no API keys required. Enjoy exploring MiroFish!
