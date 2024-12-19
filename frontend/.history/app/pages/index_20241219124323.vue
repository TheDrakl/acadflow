<template>
    <section class="flex items-center justify-between mb-10">
      <h1 class="text-4xl font-extrabold">
        Summary
      </h1>
      <div>
        <USelectMenu v-model="selectedView" :options="transactionViewOptions" />
      </div>
    </section>
  
    <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 sm:gap-16 mb-10">
    </section>
  
    <section>
      <Transaction v-for="transaction in transactions" :key="transaction.id" :transaction="transaction"/>
    </section>
  </template>
  