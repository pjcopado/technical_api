import random
import json

from . import schemas as sch, enums
from src.app.core import exceptions


class MovieService:

    def create_bulk(self, list_obj_in: list[sch.MovieCreate]):
        movies_extra = self.load_movies_file("src/app/movie/movies_extra.json")
        list_obj_in.extend(movies_extra)
        new_rating_webs = [
            enums.RatingWebsiteEnum.SCREENRANK,
            enums.RatingWebsiteEnum.CINEMASCOPE,
            enums.RatingWebsiteEnum.REELREVIEWS,
        ]
        movies = []
        for obj_in in list_obj_in:
            if "Leonardo DiCaprio" not in obj_in.actors:
                continue
            new_ratings = random.sample(range(5, 10 + 1), len(new_rating_webs))
            obj_in_dict = obj_in.model_dump()
            for web, rating in zip(new_rating_webs, new_ratings):
                obj_in_dict["ratings"][web] = rating
            obj_in_dict["ratings"] = dict(sorted(obj_in_dict["ratings"].items(), key=lambda item: item[1], reverse=True))
            obj_in_dict["rating_mean"] = round(sum(obj_in_dict["ratings"].values()) / len(obj_in_dict["ratings"]), 1)
            movies.append(obj_in_dict)
        movies.sort(key=lambda x: x["name"])
        return movies

    def load_movies_file(self, file_path: str):
        with open(file_path, "r") as file:
            data = json.load(file)
        movies = []
        for item in data:
            try:
                movie = sch.MovieCreate(**item)
            except ValueError as e:
                raise exceptions.CustomError(detail="invalid data")
            else:
                movies.append(movie)
        return movies
