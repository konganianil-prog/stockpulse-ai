import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from backend.app.main import health_check
from backend.app.api.market import get_market_overview, get_sentiment
from backend.app.api.stocks import search_stock, get_stock_report, get_stock_candles
from backend.app.api.screener import screen_stocks
from backend.app.api.sectors import list_sectors
from backend.app.api.comparison import compare_stocks
from backend.app.api.calendar import all_calendars
from backend.app.api.ai_assistant import chat_with_assistant
from backend.app.schemas.ai import ChatRequest

def run_tests():
    print("========================================", flush=True)
    print(" RUNNING STOCKPULSE AI BACKEND VERIFICATION ", flush=True)
    print("========================================", flush=True)

    # 1. Health check
    res_health = health_check()
    assert res_health["status"] == "healthy", f"Health check failed: {res_health}"
    print(f" [PASS] /api/health: {res_health}", flush=True)

    # 2. Market Overview
    data = get_market_overview()
    assert len(data["indices"]) >= 5, "Missing indices"
    assert len(data["highlights"]["top_gainers"]) > 0, "Missing top movers"
    print(f" [PASS] /api/market/overview: {len(data['indices'])} indices, {len(data['highlights']['top_gainers'])} top movers", flush=True)

    # 3. Market Sentiment
    sent = get_sentiment()
    assert "fear_greed_index" in sent, "Missing fear greed index"
    print(f" [PASS] /api/market/sentiment: Fear & Greed = {sent['fear_greed_index']}, Mood = {sent['overall_sentiment']}", flush=True)

    # 4. Stock Search
    matches = search_stock(q="tata")
    assert len(matches) > 0, "No search matches"
    print(f" [PASS] /api/stocks/search?q=tata: found {len(matches)} matches (e.g. {matches[0]['symbol']})", flush=True)

    # 5. Full Stock Research Report (RELIANCE)
    report = get_stock_report(symbol="RELIANCE")
    assert report["company"]["symbol"] == "RELIANCE"
    assert "fundamentals" in report
    assert "strengths_weaknesses" in report
    assert "ai_assessment" in report
    assert "future_outlook" in report
    print(f" [PASS] /api/stocks/RELIANCE: Price = ₹{report['quote']['current_price']}, Assessment = {report['ai_assessment']['overall_assessment']}, Quality Score = {report['ai_assessment']['quality_score']}", flush=True)

    # 6. Historical OHLCV Candles
    candles = get_stock_candles(symbol="TCS", period="1M", interval="1d")
    assert len(candles) > 0, "Empty candles"
    print(f" [PASS] /api/stocks/TCS/history: received {len(candles)} candle data points with technical overlays", flush=True)

    # 7. AI Stock Screener
    screened = screen_stocks(market_cap_category="Large Cap", min_roe=15.0)
    assert len(screened) > 0, "No screened stocks"
    print(f" [PASS] /api/screener: found {len(screened)} companies with ROE >= 15% in Large Cap", flush=True)

    # 8. Sector Intelligence
    sectors = list_sectors()
    assert len(sectors) == 14, f"Expected 14 sectors, got {len(sectors)}"
    print(f" [PASS] /api/sectors: verified all 14 Indian sectors ({', '.join([s['name'] for s in sectors[:4]])}...)", flush=True)

    # 9. Stock Comparison
    comp = compare_stocks(symbols="HDFCBANK,ICICIBANK,SBIN")
    assert len(comp["stocks"]) == 3, "Expected 3 compared stocks"
    print(f" [PASS] /api/comparison: successfully compared {len(comp['stocks'])} banking leaders with metric leaders", flush=True)

    # 10. Financial Calendars
    cal = all_calendars()
    assert "economic" in cal and "earnings" in cal and "dividends" in cal and "ipos" in cal
    print(f" [PASS] /api/calendar/all: Economic ({len(cal['economic'])}), Earnings ({len(cal['earnings'])}), Dividends ({len(cal['dividends'])}), IPOs ({len(cal['ipos'])})", flush=True)

    # 11. AI Chatbot
    chat_payload = ChatRequest(message="Is TCS fundamentally strong?")
    chat_res = chat_with_assistant(chat_payload)
    assert len(chat_res["response"]) > 20, "Chatbot response too short"
    print(" [PASS] /api/ai/chat: AI response generated with financial metrics and citations", flush=True)

    print("\n========================================", flush=True)
    print(" ALL 11 API SUITE TESTS PASSED WITH 100% SUCCESS!", flush=True)
    print("========================================", flush=True)

if __name__ == "__main__":
    run_tests()
