from flask import Flask,jsonify , request
import csv

allMovies=[]
with open ("movies.csv",encoding="utf-8") as movies:
    reader=csv.reader(movies)
    data=list(reader)
    allMovies=data[1:]
likedMovies=[]
notLikedMovies=[]
didntWatched=[]

app=Flask(__name__)

@app.route("/get-movie")
def getMovie():
    return jsonify({
        "data":allMovies[0],
        "status":"success"
    })
    
@app.route("/liked-movie",methods=["POST"])
def likedMovie():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    likedMovies.append(movie)

    return jsonify({
        "status":"success"
    }),201
@app.route("/unLiked-movie",methods=["POST"])
def unLikedMovie():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    notLikedMovies.append(movie)

    return jsonify({
        "status":"success"
    }),
@app.route("/didnt-watch",methods=["POST"])
def notWatched():
    movie=allMovies[0]
    allMovies=allMovies[1:]
    didntWatched.append(movie)

    return jsonify({
        "status":"success"
    }),201
if __name__=="__main__":
    app.run()



