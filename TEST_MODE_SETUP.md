# Test Mode Setup - Implementation Summary

## Overview

MiroFish has been configured to run in **TEST_MODE**, allowing you to test all features without needing external API keys (LLM, Zep). The system generates realistic mock data automatically.

## What Was Changed

### 1. Configuration (`/backend/app/config.py`)
- Added `TEST_MODE` configuration parameter
- Updated validation to make API keys optional when `TEST_MODE=true`
- Configuration loads from `.env` file

### 2. Test Data Generator (`/backend/app/services/test_data_generator.py`) - NEW FILE
Complete mock data generation system with:
- **MockEntity** class for individual entity objects
- **MockEntityCollection** class for entity groups
- **TestDataGenerator** class with static methods:
  - `generate_entities()` - Create mock entities by type
  - `generate_mock_profiles()` - Reddit profiles with personality/behavior
  - `generate_mock_twitter_profiles()` - Twitter profiles (CSV format)
  - `generate_mock_simulation_config()` - OASIS simulation configuration
  - `generate_mock_graph_entities()` - Complete graph with entities and relationships
  - `generate_mock_task_status()` - Task progress tracking

### 3. API Endpoints (`/backend/app/api/simulation.py`)
Modified to support test mode:

#### `/api/simulation/entities/<graph_id>` (GET)
- **Test Mode**: Returns 10 mock entities with relationships
- **Real Mode**: Queries Zep API
- Optional filtering by entity_types query parameter

#### `/api/simulation/entities/<graph_id>/<entity_uuid>` (GET)
- **Test Mode**: Returns single mock entity details
- **Real Mode**: Queries Zep API

#### `/api/simulation/entities/<graph_id>/by-type/<entity_type>` (GET)
- **Test Mode**: Returns 5 mock entities of specified type
- **Real Mode**: Queries Zep API

### 4. Environment File (`/.env`) - NEW FILE
```env
TEST_MODE=true
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```

## How to Use

### Start in Test Mode (Current Configuration)
```bash
npm run dev
```
This runs both backend and frontend. All API calls return mock data.

### Test with Specific Features
```bash
# Just backend (Python)
cd backend && python run.py

# Just frontend (Vue.js)
cd frontend && npm run dev
```

### Test API Directly
```bash
# Get mock graph entities
curl http://localhost:5001/api/simulation/entities/demo_graph

# Get mock entity details
curl http://localhost:5001/api/simulation/entities/demo_graph/entity_123

# Get mock entities by type
curl http://localhost:5001/api/simulation/entities/demo_graph/by-type/Student

# With filters
curl "http://localhost:5001/api/simulation/entities/demo_graph?entity_types=Student,PublicFigure"
```

## Switching Between Modes

### To Enable Real API Mode:
1. Add your actual API keys to `.env`:
   ```env
   LLM_API_KEY=sk-your-actual-key
   ZEP_API_KEY=your-zep-key
   ```

2. Set TEST_MODE to false:
   ```env
   TEST_MODE=false
   ```

3. Restart the backend

### To Return to Test Mode:
1. Set TEST_MODE back to true in `.env`
2. Restart the backend
3. No API keys needed!

## Mock Data Characteristics

### Entity Data
- Names are realistic (Alice Johnson, Elon Musk, TechCorp Inc, etc.)
- Types include: Student, PublicFigure, Organization, Location, Topic
- Properties: age, location, interests
- Deterministic IDs: `entity_xxxxx`

### Graph Data
- Realistic relationship edges (knows, works_with, collaborates)
- Entity type distribution
- Enriched with relationship information

### Profile Data
- Reddit: username, personality, behavior, interests, posting_frequency, engagement_level
- Twitter: handle, profile_type, personality, behavior, engagement_level (CSV format)

### Simulation Config
- Configurable max_rounds (default: 10)
- Platform support: reddit, twitter
- Parameter sets: posts/tweets per round, interaction probabilities

## File Locations

**New Files:**
- `/backend/app/services/test_data_generator.py` - Test data generation
- `/.env` - Environment configuration
- `/TESTING_GUIDE.md` - Comprehensive testing documentation
- `/TEST_MODE_SETUP.md` - This file

**Modified Files:**
- `/backend/app/config.py` - Added TEST_MODE config
- `/backend/app/api/simulation.py` - Added test mode checks

## Architecture

```
API Request
    ↓
Config.TEST_MODE check
    ↓
├─ TRUE: TestDataGenerator.generate_*()  → Mock Data
│
└─ FALSE: Real API Call (LLM/Zep) → Real Data
```

## Error Handling

- If TEST_MODE=false and API keys missing: Returns 500 with "API key missing" error
- If TEST_MODE=true: Always returns mock data (keys optional)
- Graceful fallback with appropriate error messages

## Performance Notes

- Mock data is generated fresh on each request (realistic for testing)
- No API calls = no latency when in TEST_MODE
- Full feature testing without hitting rate limits
- Ideal for development, CI/CD testing, and demos

## Next Steps

1. ✅ Test mode is enabled and ready to use
2. Run `npm run dev` to start both services
3. Access frontend at http://localhost:5173
4. Backend APIs available at http://localhost:5001
5. Add real API keys when ready for production testing

## Debugging

Enable verbose logging:
```bash
# Check backend logs
FLASK_DEBUG=true npm run backend

# Frontend console logs
npm run frontend
```

Test a specific endpoint:
```bash
# Terminal 1: Start backend
cd backend && python run.py

# Terminal 2: Test endpoints
curl -v http://localhost:5001/api/simulation/entities/test
```
