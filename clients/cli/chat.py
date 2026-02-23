import argparse
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Optional

@dataclass
class ChatConfig:
    base_url: str
    user_id: str
    target_language: str
    mode:str

def post_json(url: str, payload: dict) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} error from server:\n{err_body}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Could not reach server at {url}: {e}") from e

def chat_loop(cfg: ChatConfig) -> None:
    chat_url = cfg.base_url.rstrip("/") + "/chat"

    print("ChatterMate CLI")
    print(f"- Server: {cfg.base_url}")
    print(f"- user_id: {cfg.user_id}")
    print(f"- target_language: {cfg.target_language}")
    print(f"- mode: {cfg.mode}")
    print("Type your message and press Enter. Type /quit to exit.\n")

    conversation_id: Optional[str] = None

    while True:
        try:
            text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not text:
            continue
        if text.lower() in {"/quit", "/exit"}:
            print("Bye!")
            return

        payload = {
            "user_id": cfg.user_id,
            "target_language": cfg.target_language,
            "mode": cfg.mode,
            "text": text,
        }
        if conversation_id:
            payload["conversation_id"] = conversation_id

        resp = post_json(chat_url, payload)

        conversation_id = resp.get("conversation_id", conversation_id)
        assistant_text = resp.get("assistant_text", "")
        print(f"Mate: {assistant_text}")

        corrections = resp.get("corrections") or []
        if corrections:
            print("\nCorrections:")
            for c in corrections:
                original = c.get("original", "")
                corrected = c.get("corrected", "")
                explanation = c.get("explanation")
                print(f"- {original} -> {corrected}")
                if explanation:
                    print(f"  {explanation}")
            print()


def parse_args() -> ChatConfig:
    p = argparse.ArgumentParser(description="ChatterMate CLI client")
    p.add_argument("--base-url", default="http://127.0.0.1:8000", help="FastAPI base URL")
    p.add_argument("--user-id", default="anon", help="User identifier")
    p.add_argument("--lang", default="en", help="Target language code (e.g. en, fr, de)")
    p.add_argument("--mode", default="casual", choices=["casual", "professional"], help="Conversation mode")
    args = p.parse_args()

    return ChatConfig(
        base_url=args.base_url,
        user_id=args.user_id,
        target_language=args.lang,
        mode=args.mode,
    )

def main() -> None:
    cfg = parse_args()
    try:
        chat_loop(cfg)
    except RuntimeError as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
