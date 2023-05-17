import Axios from "axios";
import { useState, useEffect } from "react";
import Typography from '@mui/material/Typography'


const Posts = () => {
  const [blogPosts, setBlogPosts] = useState([]);

  useEffect(() => {
    const getData = () => {
      Axios.get("http://127.0.0.1:8000/api/blog/posts/").then((res) => {
        setBlogPosts(res.data);
      });
    };
    getData();
  }, []);

  return (
    <>
      {blogPosts.map((post) => (
        <div key={post.id}>
          <Typography variant="h1">{ post.title }</Typography>
          <Typography variant="body1">{ post.content }</Typography>
        </div>
      ))}
    </>
  );
};

export default Posts;
