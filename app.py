from flask import Flask, jsonify, render_template
import itertools
import random

app = Flask(__name__)

# 트럼프 카드 덱 생성 함수
def create_shuffled_deck():
    suits = {'♠': 'spades', '♥': 'hearts', '♦': 'diamonds', '♣': 'clubs'}
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit, f"/static/cards/{rank}{suits[suit]}.png") for rank, suit in itertools.product(ranks, suits)]
    random.shuffle(deck)
    return deck

# 5개의 테이블마다 독립적인 덱 생성
tables = {i: create_shuffled_deck() for i in range(1, 6)}

@app.route('/')
def home():
    """메인 페이지 렌더링"""
    return render_template('index.html', tables=list(tables.keys()))

@app.route('/draw/<int:table_id>', methods=['GET'])
def draw_card(table_id):
    """특정 테이블에서 한 장의 카드를 뽑아 JSON으로 반환"""
    if table_id not in tables:
        return jsonify({"error": "존재하지 않는 테이블 ID입니다."})

    deck = tables[table_id]

    if not deck:
        tables[table_id] = create_shuffled_deck()
        deck = tables[table_id]

    drawn_card = deck.pop()
    return jsonify({"table_id": table_id, "drawn_card": drawn_card})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
