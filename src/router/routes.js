const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("src/pages/Home.vue")
      },
      {
        path: "/getstarted",
        component: () => import("src/pages/PickFile.vue")
      },
      {
        path: "/camera",
        component: () => import("src/pages/TakePhoto.vue")
      },
      {
        path: "/solution",
        component: () => import("src/pages/Solution.vue")
      },
      {
        path: "/planthealthy",
        component: () => import("src/pages/PlantHealthy.vue")
      },
      {
        path: "/symptoms",
        component: () => import("src/pages/Symptoms.vue")
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "*",
    component: () => import("pages/Error404.vue")
  }
];

export default routes;
