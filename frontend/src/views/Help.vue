<template>
  <div id="help">
  <section class="section">
    <div class="container">
      <h1 class="title">Golinks Help</h1>
      <h2 class="subtitle">
        This section will explain <strong>Golinks</strong> and  how to use them
      </h2>
    </div>

    <div class="content article-body">
      <p></p>
      <h3>What are Golinks?</h3>
      <p>It’s an internal URL shortener common to many tech companies. Golinks were created at Google by <a href="https://twitter.com/bstaffin">@bstaffin</a>.
        If you’re on the company network, you can type in <code>go/keyword</code> in your browser, and that will redirect you to some other site.
        Yahoo uses  <code>yo/links</code>, Dropbox uses <code>drl/links</code> and lyft uses <code>go.lyft/links</code>
      <p></p>
      <h3>How do I see whats behind a link?</h3>
      <p>
      <p>You can preview what lies behind a short link. Add a <code>+</code> at the end of your link to view more about it before being redirected</p>
      <h3>How do nested keywords work?</h3>
      <p>
      <p>Nested keywords like <code>eng/handbook</code> and <code>eng/help</code> group together and get a landing page at <code>eng</code></p>
      <h3>How do programmatic links work?</h3>
      <p>
      <p>Create short links that inject variables by using <code>%s</code>.  For example: <code>gh/%s</code> to link to <code>github.com/%s</code></p>


    </div>

  </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  components: {
  },
  data() {
    return {
    };
  },
  methods: {
  },
  created() {
  }
};
</script>
<style>
#help {
  text-align: left;
}
</style>
